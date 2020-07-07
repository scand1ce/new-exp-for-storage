from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Файл', blank=False)
    objects = models.Manager()