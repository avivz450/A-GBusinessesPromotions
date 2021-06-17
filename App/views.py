from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale, Profile, Business, Website
from .forms import SignUpForm, BusinessForm, SaleForm, ChooseWebsiteForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def websitepage(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    context = {
        "website": website,
    }
    return render(request, "home/websitepage.html", context)


def landingpage(request):
    if request.method == "POST":
        form = ChooseWebsiteForm(request.POST)
        if form.is_valid():
            selected_website_id = request.POST.get("website")
            selected_website = Website.objects.filter(id=selected_website_id).first()
            return redirect("websitepage", selected_website.id, selected_website.name)
    else:
        form = ChooseWebsiteForm()
    return render(request, "home/landingpage.html", {"form": form, "title": "Welcome!"})


def businesses(request, pk, website_name):
    if request.method == "GET":
        context = {
            "businesses": Business.objects.all(),
            "website": get_object_or_404(Website, id=pk),
        }
    return render(request, "home/businesses.html", context)


def sales(request, pk, website_name):
    if request.method == "GET":
        context = {
            "sales": Sale.objects.all(),
            "website": get_object_or_404(Website, id=pk),
        }
    return render(request, "home/sales.html", context)


def signup(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user.save()
            profile = Profile(user=user)
            user = authenticate(username=user.username, password=raw_password)
            profile.save()
            profile.match_website_to_profile(website)
            login(request, user)
            return redirect("websitepage", website.id, website.name)
    else:
        form = SignUpForm()
    return render(
        request,
        "home/signup.html",
        {
            "form": form,
            "title": "Sign Up",
            "website": website,
        },
    )


def new_business(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        num_of_businesses_of_profile = len(
            Business.objects.filter(profile=logged_in_profile)
        )

        if logged_in_profile.is_vip or num_of_businesses_of_profile == 0:
            if request.method == "POST":
                businessForm = BusinessForm(request.POST, request.FILES)
                if businessForm.is_valid():
                    businessForm = businessForm.save(commit=False)
                    businessForm.profile = logged_in_profile
                    businessForm.save()
                    msg_content = """The business was successfully inserted.
                It will be visible once the site administrators will approve it."""
                    messages.info(
                        request,
                        {
                            "title": "INFO: ",
                            "message_content": msg_content,
                        },
                    )
                    return render(
                        request,
                        "home/websitepage.html",
                        {
                            "title": "Welcome!",
                            "website": website,
                        },
                    )
            else:
                form = BusinessForm()
                return render(
                    request,
                    "home/new_business.html",
                    {
                        "form": form,
                        "title": "New Business",
                        "website": website,
                    },
                )
        else:
            messages.error(
                request,
                {
                    "title": "ERROR: ",
                    "message_content": "You must be a Premium member to submit more than one business.",
                },
            )

        return render(
            request,
            "home/websitepage.html",
            {
                "title": "Welcome!",
                "website": website,
            },
        )


def premium(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        if request.method == "POST":
            if "vip_user" in request.POST:
                logged_in_profile.is_vip = True
                logged_in_profile.save(update_fields=["is_vip"])
                messages.success(
                    request,
                    {
                        "title": "SUCCESS: ",
                        "message_content": "Congratulations, you are a Premium user now!",
                    },
                )
            return render(
                request,
                "home/websitepage.html",
                {
                    "title": "Welcome!",
                    "website": website,
                },
            )
        elif logged_in_profile.is_vip is True:
            messages.info(
                request,
                {
                    "title": "INFO: ",
                    "message_content": "You are already a Premium user.",
                },
            )
            return render(
                request,
                "home/websitepage.html",
                {
                    "title": "Welcome!",
                    "website": website,
                },
            )
        else:
            return render(
                request,
                "home/premium.html",
                {
                    "title": "AG Premium",
                    "website": website,
                },
            )


def new_sale(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
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
                    msg_content = """The sale was successfully inserted.
                It will be visible once the site administrators will approve it."""
                    messages.info(
                        request,
                        {
                            "title": "INFO: ",
                            "message_content": msg_content,
                        },
                    )
                    return render(
                        request,
                        "home/websitepage.html",
                        {
                            "title": "Welcome!",
                            "website": website,
                        },
                    )
            return render(
                request,
                "home/new_sale.html",
                {
                    "form": form,
                    "title": "New Sale",
                    "website": website,
                },
            )
        else:
            messages.error(
                request,
                {
                    "title": "ERROR: ",
                    "message_content": "You must be a Premium member to submit more than one sale.",
                },
            )
            return render(
                request,
                "home/websitepage.html",
                {
                    "title": "Welcome!",
                    "website": website,
                },
            )


def business_page(request, pk, business_name):
    business = get_object_or_404(Business, id=pk)
    context = {
        "business": business,
    }
    return render(request, "home/business_page.html", context)


def login_view(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    form = AuthenticationForm()

    if request.method == "GET":
        return render(
            request,
            "home/login.html",
            {
                "website": website,
                "form": form,
            },
        )
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("websitepage", website.id, website.name)
        else:
            messages.error(
                request,
                {
                    "title": "ERROR: ",
                    "message_content": "Invalid username/password.",
                },
            )
            return render(
                request,
                "home/login.html",
                {
                    "website": website,
                    "form": form,
                },
            )
