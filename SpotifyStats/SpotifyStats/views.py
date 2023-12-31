from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'login.html')