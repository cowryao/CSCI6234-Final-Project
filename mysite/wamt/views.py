from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name="wamt/index.html",
                  context={"movies": Movie.objects.all})


def register(request):
    print("I do register")
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("the form is good")
            user = form.save()
            login(request, user)
            return redirect("/")

    form = UserCreationForm
    return render(request=request, 
                  template_name="wamt/register.html",
                  context={"form": form})