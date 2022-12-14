from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReviewForm, ClientForm
from .models import Review, Client, User
import datetime
from django.core.mail import send_mail


def test(request):
    return render(request, 'test.html')


def home(request):
    return render(request, 'home.html')

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
            allReviews = Review.objects.order_by('-datecreated')
            reviews = allReviews[:3]
            if reviews:
                totalReviews = reviews.__len__()
                averageReviews = 0
                for review in reviews:
                    averageReviews += review.rating
                    formatedReviews = []
                    review.datecreated = review.datecreated.strftime("%B %d, %Y")
                    userName = review.user
                    userName = userName[0]
                    review.userName = userName
                    for rating in range(review.rating):
                        formatedReviews.append("")
                        review.rating = formatedReviews
                averageReviews /= totalReviews
                averageReviews = int(averageReviews)
                formatedAverageReviews = []
                for average in range(averageReviews):
                    formatedAverageReviews.append("")
                return render(request, 'home.html', {
                    "totalReviews": totalReviews,
                    "averageReviews": formatedAverageReviews,
                    "reviews": reviews
                })
            return render(request,'home.html')


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
                userName = review.user
                userName = userName[0]
                review.userName = userName
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
        guest = request.POST.get('guest')
        if guest == None:
            user = request.user
        title = request.POST['title']
        description = request.POST['description']
        if rating == "":
            return render(request, 'addReview.html', {'errors': "you must choose a star rating"})
        elif guest == "":
            return render(request, 'addReview.html', {'errors': "you must enter your guest name"})
        elif title == "":
            return render(request, 'addReview.html', {'errors': "you must enter a title"})
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

def clients(request):
    if request.method == 'GET':
        user = str(request.user)
        clients = Client.objects.all()
        totalClients = clients.__len__()
        if user == "JacktockinLacktoz":
            return render(request, 'clients.html', {"clients": clients, "totalClients": totalClients})
        else:
            return redirect("/login")

def terms(request):
    if request.method == 'GET':
        return render(request, 'terms.html')

def addClient(request):
    if request.method == 'GET':
        return render(request, 'addClient.html')
    else:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        size = request.POST['size']
        rooms = request.POST['rooms']
        message = f"name: {name}\ntelephone number: {phone}\nemail address: {email}\nhome address: {address}\nhome squre feet: {size}\nhome rooms: {rooms}"
        terms = request.POST.get("terms")

        if name == "" and phone == "" or name == "" and email == "":
            return render(request, 'addClient.html', {'errors': "you must enter your name and phone number or email"})

        elif terms == 'on':
            try:
                client = ClientForm(request.POST)
                client.save()
                send_mail(
                    "new client",
                    message,
                    'marianashousecleaningllc@outlook.com',
                    ['marianashousecleaningllc@gmail.com'])
                return redirect('/')
            except ValueError:
                return render(request, 'home.html', {'errors': "you entered in bad information"})
        else:
            return render(request, 'addClient.html', {'errors': "you didn't enter any fields"})

def payment(request):
    return render(request, 'payment.html')


def createSession(request):
    YOUR_DOMAIN = 'http://localhost:8000'
    if request.method == 'POST':
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': '0.01',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
                automatic_tax={'enabled': True},
            )
            print('success')
        except Exception as e:
            print(e)
            print('************************************')
            return redirect('/payment')
        return redirect(checkout_session.url, code=303)
    if request.method == 'GET':
        redirect('/method')
