from django.db import models


class UserAccount(models.Model):
    pass


class UploadFile(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

