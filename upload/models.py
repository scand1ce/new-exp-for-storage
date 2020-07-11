from django.db import models


class UserAccount(models.Model):
    pass


class File(models.Model):
    file = models.FileField(upload_to='upload/files/%Y/%m/%d/', verbose_name='Файл', blank=False)
    objects = models.Manager()
