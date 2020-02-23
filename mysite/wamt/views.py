from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, NewUserManager, NewGroupManager
from .forms import NewUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages
# Create your views here.


def add_new_group(request):
    try:
        # filter is getting all the objects, however the result are querysets
        # get is getting a instance of class, however it will raise error when the instance cannot be found
        # the parameter in filter and get is object and its parameters such as NewUserManager->NewUserManager:user->User:username
        usermanager = NewUserManager.objects.filter(user__username="zheming3")
        group = Group.objects.get(name="group2")
        print(vars(usermanager))
        for u in usermanager.all():
            # print(vars(u))
            print(u.group_owned.all())
            # u.group_owned.add(* group)  //if group is a query set
            u.group_owned.add(group)
            u.save()
            print(u.group_owned.all())
            u.group_owned.remove(group)
            u.save()
            print(u.group_owned.all())
        # print(dir(user))
    except Exception as e:
        print("meet error")


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
