from django.db import models


class UserAccount(models.Model):
    pass


class File(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Файл', blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
