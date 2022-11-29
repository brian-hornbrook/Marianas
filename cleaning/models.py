from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Review (models.Model):
    rating = models.IntegerField(max_length=10)
    user = models.CharField(max_length=100, default=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000)
    datecreated = models.DateField(default=timezone.now())
    def __str__(self):
        return self.title

class Client (models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    size = models.CharField(max_length=100)
    rooms = models.CharField(max_length=100)
    def __str__(self):
        return self.name