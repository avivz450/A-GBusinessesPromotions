from django.shortcuts import render, redirect
from .models import Sale, Profile, Business
from .forms import SignUpForm, BusinessForm, SaleForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.
def landingpage(request):
    return render(request, "home/landingpage.html", {"title": "Welcome!"})


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
    logged_in_profile = Profile.objects.filter(user=request.user).first()
    num_of_businesses_of_profile = len(
        Business.objects.filter(profile=logged_in_profile)
    )

    if logged_in_profile.is_vip or num_of_businesses_of_profile == 0:
        form = BusinessForm
        if request.method == "POST":
            businessForm = BusinessForm(request.POST, request.FILES)
            if businessForm.is_valid():
                businessForm = businessForm.save(commit=False)
                businessForm.profile = logged_in_profile
                businessForm.save()
                return redirect("/")
        return render(
            request, "home/new_business.html", {"form": form, "title": "New Business"}
        )
    else:
        messages.error(
            request,
            {
                "title": "ERROR: ",
                "message_content": "You must be a VIP member to submit more than one business.",
            },
        )
        return render(request, "home/landingpage.html", {"title": "Welcome!"})


def new_sale(request):
    logged_in_profile = Profile.objects.filter(user=request.user).first()
    num_of_sales_of_profile = len(Sale.objects.filter(profile=logged_in_profile))

    if logged_in_profile.is_vip or num_of_sales_of_profile == 0:
        form = SaleForm(logged_in_user=request.user.id)
        if request.method == "POST":
            saleForm = SaleForm(
                request.POST, request.FILES, logged_in_user=request.user.id
            )
            if saleForm.is_valid():
                saleForm = saleForm.save(commit=False)
                saleForm.profile = logged_in_profile
                saleForm.save()
                return redirect("/")
                return render(
                    request, "home/new_sale.html", {"form": form, "title": "New Sale"}
                )
    else:
        messages.error(
            request,
            {
                "title": "ERROR: ",
                "message_content": "You must be a VIP member to submit more than one sale.",
            },
        )
        return render(request, "home/landingpage.html", {"title": "Welcome!"})
