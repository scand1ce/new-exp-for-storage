
from django.urls import path


from .views import *
# from upload import views

urlpatterns = [
    path('', upload_files, name='upload_files'),
    path('list_files/', list_files, name='list_files'),
    path('upload/', upload, name='user'),



]

