from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from main.models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()  

    class Meta: 
        model = User
        fields = ["username","email","password1","password2"]

class PictureForm(forms.ModelForm):
  
    class Meta:
        model = Profile
        fields = ['avatar']

