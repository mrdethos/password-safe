from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/signup.html')