from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import File


class HomePageView(ListView):
    model = File
    template_name = 'home.html'


class CreatePostView(CreateView): # новый
    model = File
    #form_class = PostForm
    #template_name = 'post.html'
    success_url = reverse_lazy('home')