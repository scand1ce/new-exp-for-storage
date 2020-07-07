from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Main Page</h1>')



def login(request):

    return HttpResponse('<h1>LOGIN</h1>')


def reg(request):

    return HttpResponse('<h1>REG</h1>')



