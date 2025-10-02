from django import forms
from .models import Gig
from .models import TaskRequest


class GigForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'description', 'category', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'category': forms.Select(),
        }

class TaskRequestForm(forms.ModelForm):
    class Meta:
        model = TaskRequest
        fields = ['location', 'details']
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Enter your location'}),
            'details': forms.Textarea(attrs={'placeholder': 'Describe your task'}),
        }
