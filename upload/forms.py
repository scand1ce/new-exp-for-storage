from django import forms
from .models import UploadFile


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('number', 'comment', 'file')
