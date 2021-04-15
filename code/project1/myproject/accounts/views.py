from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from analytics.models import Session
from datetime import datetime, timezone
from categories.models import Category

#Create an empty field for a new user at Category model
def initialise_cat(username):
    category = Category()
    category.username = username
    category.type = '-'
    category.save()

#Register users. S
def register(request):
    if request.method == 'POST':
        # GET form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check if passwords match
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Everything is fine for the registration.
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    initialise_cat(username)
                    messages.success(
                        request, 'You are now registered and can login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

#Store start time to the Session database
def start_session(username):
    session = Session()
    session.username = username
    session.start_time = datetime.now(timezone.utc)
    session.end_time = datetime.now(timezone.utc)
    session.save()

#Store end time to the Session database and calculate duration
def stop_session(request):
    username = request.user.username
    queryset = Session.objects.filter(username=username,done=False)
    obj = get_object_or_404(queryset)
    obj.done = True
    obj.end_time = datetime.now(timezone.utc)
    obj.duration = obj.end_time - obj.start_time
    obj.save()

#Check if the login is valid or not
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            start_session(username)
            return redirect('questions')
        else:
            messages.error(request, 'Invalid crendentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

#Proceed to log out once the logout button is pressed
def logout(request):
    if request.method == "POST":
        stop_session(request)
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home')
