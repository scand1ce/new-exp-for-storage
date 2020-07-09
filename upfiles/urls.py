from django.urls import path, include
from .views import *


urlpatterns = [
    path('', reg, name='registration'),
    path('login/', login, name='login'),
    path('upload/', index, name='home'),


]


