from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from categories.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from flask import redirect
#Link to url.py
def home(request):
    return render(request, "home.html",{})
#Pass the product (exhibit items) details to shop.html
def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html",{'products':products})
#Pass the persona of the user, the product details and the verification to altern the interface to the product_page.html
def product_page(request,listing_id):
    product_page = get_object_or_404(Product, pk=listing_id)
    username = request.user.username
    queryset = Category.objects.filter(username=username)
    this = get_object_or_404(queryset)
    category = this.type 
    verified = this.verified
    context = {'product_page': product_page,'category':category,'verified':verified}
    return render(request, 'product_page.html', context)
