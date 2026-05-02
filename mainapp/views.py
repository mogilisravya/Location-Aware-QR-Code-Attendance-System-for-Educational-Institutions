from django.shortcuts import render, redirect

# Create your views here.

# Home Page
def home(req):
    return render(req, 'main/index.html')

# Contact Us
def contactUs(req):
    return render(req, 'main/main-contact.html')

# About Us
def aboutUs(req):
    return render(req, 'main/main-about.html')

