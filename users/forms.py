from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2', 'is_seller']
