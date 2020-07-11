from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(upload_to='upload/files/%Y/%m/%d/', verbose_name='Файл', blank=False)
    title = forms.CharField(max_length=50, required=False)

