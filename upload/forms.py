from django import forms
from .models import UploadFile


class UploadForm(forms.Form):
    class Meta:
        model = UploadFile
        fields = '__all__'
