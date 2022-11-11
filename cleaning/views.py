from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReviewForm
from .models import Review
import datetime


def signupUser(request):
    if request.method == 'GET':
        return render(request, 'signupUser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'signupUser.html', {'form': UserCreationForm(), 'errors': "that username or password was already taken"})
        else:
            return render(request, 'signupUser.html', {'form': UserCreationForm(), 'errors': "your passwords did not match"})


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        errors = ""
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "login.html", {"form": AuthenticationForm(), "errors": "username or password doesn't exists"})
        else:
            login(request, user)
            return redirect('/')


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        return render(request, 'home.html')


def home(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        if reviews:
            totalReviews = reviews.__len__()
            averageReviews = 0
            for review in reviews:
                averageReviews += review.rating
                formatedReviews = []
            averageReviews /= totalReviews
            averageReviews = int(averageReviews)
            formatedAverageReviews = []
            for average in range(averageReviews):
                formatedAverageReviews.append("")

            return render(request, 'home.html', {
                "totalReviews": totalReviews,
                "averageReviews": formatedAverageReviews
            })
        return render(request,'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def reviews(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        if reviews:
            totalReviews = reviews.__len__()
            averageReviews = 0
            for review in reviews:
                averageReviews += review.rating
                formatedReviews = []
                review.datecreated = review.datecreated.strftime("%B %d, %Y")
                for rating in range(review.rating):
                    formatedReviews.append("")
                    review.rating = formatedReviews
            averageReviews /= totalReviews
            averageReviews = int(averageReviews)
            formatedAverageReviews = []
            for average in range(averageReviews):
                formatedAverageReviews.append("")

            return render(request, 'reviews.html', {
                "reviews": reviews,
                "totalReviews": totalReviews,
                "averageReviews": formatedAverageReviews
            })
        else:
            return render(request, 'reviews.html')


def addReview(request):
    if request.method == 'GET':
        return render(request, 'addReview.html')
    else:
        rating = request.POST['rating']
        guest = request.POST['guest']
        description = request.POST['description']
        if rating == "":
            return render(request, 'addReview.html', {'errors': "you must choose a star rating"})
        elif guest == "":
            return render(request, 'addReview.html', {'errors': "you must enter your guest name"})
        elif description == "":
            return render(request, 'addReview.html', {'errors': "you must not leave the review section blank"})
        else:
            try:
                form = ReviewForm(request.POST)
                newReview = form.save(commit=False)
                if guest:
                    newReview.user = guest
                else:
                    newReview.user = request.user
                newReview.save()
                return redirect('/reviews')
            except ValueError:
                return render(request, 'addReview.html', {'errors': "you entered in bad information"})
