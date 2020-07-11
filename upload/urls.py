
from django.urls import path


from .views import *

urlpatterns = [
    path('', reg, name='registration'),
    path('login/', login, name='login'),
    path('upload/', upload, name='user'),


]


