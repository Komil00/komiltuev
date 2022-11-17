from django.db import models

# Create your models here.
from django.urls import reverse


class Otziv(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    address = models.CharField(max_length=50)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base')
