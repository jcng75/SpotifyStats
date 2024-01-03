from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'landingPage.html')

def signin(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def testNav(request):
    return render(request, 'navbar1.html')