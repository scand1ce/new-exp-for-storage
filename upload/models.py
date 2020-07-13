from django.db import models


class UploadFile(models.Model):
    number = models.IntegerField(max_length=100)
    comment = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.number





