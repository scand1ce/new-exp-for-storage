# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .models import UploadFile


class Home(TemplateView):
    template_name = 'pages/upload_files.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'pages/upload_.html',  context)


def list_files(request):
    files = UploadFile.objects.all()
    return render(request, 'pages/list_files.html', {
        'files': files
    })


def upload_files(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_files')
    else:
        form = UploadForm()

    return render(request, 'pages/upload_files.html', {
        'form': form
    })




