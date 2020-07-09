from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'pages/upload_.html')


def login(request):
    return render(request, 'pages/login.html')


def reg(request):
    return render(request, 'pages/registration.html')
