from django.shortcuts import render, redirect
from .models import Sale, Profile, Business
from .forms import SignUpForm, BusinessForm
from django.contrib.auth import login, authenticate


# Create your views here.
def landingpage(request):
    return render(request, "home/landingpage.html", {"title": "Welcome!"})


def base(request):
    return render(request, "home/base.html")


def businesses(request):
    if request.method == "GET":
        context = {"businesses": Business.objects.all()}
    return render(request, "home/businesses.html", context)


def sales(request):
    if request.method == "GET":
        context = {"sales": Sale.objects.all()}
    return render(request, "home/sales.html", context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user.save()
            profile = Profile(user=user)
            user = authenticate(username=user.username, password=raw_password)
            profile.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "home/signup.html", {"form": form, "title": "Sign Up"})


def new_business(request):
    form = BusinessForm
    if request.method == "POST":
        businessForm = BusinessForm(request.POST)
        if businessForm.is_valid():
            businessForm = businessForm.save(commit=False)
            businessForm.profile = Profile.objects.filter(user=request.user).first()
            businessForm.save()
    return render(
        request, "home/new_business.html", {"form": form, "title": "New Business"}
    )
