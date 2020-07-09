from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(upload_to='upfiles/files/%Y/%m/%d/', verbose_name='Файл', blank=False)

