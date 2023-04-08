from django.contrib.auth.forms import UsernameField
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            for x in User.objects.all():
                if form.cleaned_data["username"] == x.username: 
                    print("duplicate found")
            form.save()
        return redirect("/login/")
    else:
        form = RegisterForm()
        
    return render(response, 'register/register.html', {"form":form})

def login(response):

    return render(response, 'registration/login.html', {})

