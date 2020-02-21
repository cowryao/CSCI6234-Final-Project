from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, NewUserManager, NewGroupManager
from .forms import NewUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages
# Create your views here.


def homepage(request): 
    return render(request=request,
                  template_name="wamt/index.html",
                  context={"movies": Movie.objects.all})


def register(request):
    # print("I do register")
    if request.method == "POST":       
        form = NewUserCreationForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            # print("the form is good")
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created {username}")
            login(request, user)
            return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages}")

    form = NewUserCreationForm
    return render(request=request,
                  template_name="wamt/register.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("/login")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now loggin as {username}")
                return redirect("/")
            else: 
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid input username or password")
    form = AuthenticationForm()
    return render(request,
                  "wamt/login.html",
                  {"form": form})