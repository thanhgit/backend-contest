from django.db import models

# Create your models here.

class Logger(models.Model):
    filename = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200)
    client_ip = models.CharField(max_length=20)
    file_size = models.CharField(max_length=20)
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.filename






