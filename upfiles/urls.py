from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('reg/', reg, name='registration')
]


