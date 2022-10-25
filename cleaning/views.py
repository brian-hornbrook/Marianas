from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def signupUser(request):
    if request.method == 'GET':
        return render(request, 'signupUser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                print(user)
                login(request, user)
                return redirect('/')
            except IntegrityError:
                print('already exists')
                return render(request, 'signupUser.html', {'form': UserCreationForm(), 'errors': "that username or password was already taken"})
        else:
            print("passwords din't match")
            return render(request, 'signupUser.html', {'form': UserCreationForm(), 'errors': "your passwords did not match"})
            

def loginUser(request):
    if request.method == 'GET':
        print("loaded")
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        errors = ""
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "login.html", {"form": AuthenticationForm(), "errors": "username or password doesn't exists"})
        else:
            login(request, user)
            return redirect('/')

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
        print("did log out")
    else:
        return render(request, 'home.html')
        print("didn't logout")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def reviews(request):
    return render(request, 'reviews.html')