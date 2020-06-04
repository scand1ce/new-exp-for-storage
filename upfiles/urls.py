from django.urls import path
from . import views
from .views import HomePageView
app_name = 'upfiles'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
