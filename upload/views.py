# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

class Home(TemplateView):
    template_name = 'pages/registration.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['userdocs']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'pages/upload_.html', context)


def login(request):
    return render(request, 'pages/login.html')


def reg(request):
    return render(request, 'pages/registration.html')
