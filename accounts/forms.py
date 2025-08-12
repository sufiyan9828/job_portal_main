from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class RegisterForm(UserCreationForm):
    password = forms.CharField(max_length=25,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','contact']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25,widget=forms.PasswordInput)
