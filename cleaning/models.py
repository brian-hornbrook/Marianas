from django.db import models
from django.contrib.auth.models import User

class Review (models.Model):
    rating = models.IntegerField(max_length=10)
    user = models.CharField(max_length=100, default=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000)
    datecreated = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title