from django.db import models
from django.contrib.auth.models import User

class Review (models.Model):
    rating = models.IntegerField(max_length=10)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000)
    datecreated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title