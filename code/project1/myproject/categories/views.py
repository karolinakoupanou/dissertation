from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from flask import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#Link with url.py
def questions(request):
    return render(request, "questions.html",{})

#When the questionaire it it answered the persona is determined according to the user's answers.
def update_type_professional(request):
    if request.method == 'POST':
        question1 = request.POST['option']
        question2 = request.POST['option1']
        if ((question1 == '1') and (question2 == 'e')):
            category = Category()
            category.username = request.user.username
            category.type = 'Professional/Hobbyist'
            category.save()
        else:
            if ((question1 == '2') and (question2 == 'a')):
                category = Category()
                category.username = request.user.username
                category.type = 'Socializer Facilitator'
                category.save()
            else:
                if ((question1 == '2') and (question2 == 'b')):
                    category = Category()
                    category.username = request.user.username
                    category.type = 'Explorer'
                    category.save()
                else:
                    if ((question1 == '2') and (question2 == 'd')):
                        category = Category()
                        category.username = request.user.username
                        category.type = 'Experience Seeker'
                        category.save()
                    else:
                        if ((question1 == '3') and (question2 == 'a')):
                            category = Category()
                            category.username = request.user.username
                            category.type = 'Parental Facilitator'
                            category.save()
                        else:
                            if ((question1 == '4') and (question2 == 'c')):
                                category = Category()
                                category.username = request.user.username
                                category.type = 'Recharger'
                                category.save()
    return HttpResponseRedirect('/')
