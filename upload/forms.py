from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(upload_to='files/')
    title = forms.CharField(max_length=50, required=False)

