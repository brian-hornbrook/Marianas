from django.forms import ModelForm
from .models import Review, Client

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'description']


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email', 'address', 'size', 'rooms']
