from django.db import models
from django.contrib.auth.models import User

class Review (models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    review = models.TextField(max_length=1000)
    datecreated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title