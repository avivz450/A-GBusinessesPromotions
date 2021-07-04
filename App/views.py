from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale, Profile, Business, Website, Website_Profile, Website_Business
from .forms import (
    SignUpForm,
    BusinessForm,
    SaleForm,
    ChooseWebsiteForm,
    UserBusinessesForm,
    UserSalesForm,
)
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def websitepage(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    context = {
        "website": website,
    }
    if request.user.is_authenticated:
        website_profile_pair = Website_Profile.get_website_profile_pair(
            request.user, website
        )
        if website_profile_pair is None:
            logout(request)
        else:
            context["website_profile_pair"] = website_profile_pair

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
    website = get_object_or_404(Website, id=pk)
    context = {
        "website_business_pairs": Website_Business.objects.filter(website=website),
        "website": website,
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            context["website_profile_pair"] = Website_Profile.get_website_profile_pair(
                request.user, website
            )
    return render(request, "home/businesses.html", context)


def sales(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    context = {
        "sales": Sale.objects.all(),
        "website": website,
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            context["website_profile_pair"] = Website_Profile.get_website_profile_pair(
                request.user, website
            )
    return render(request, "home/sales.html", context)


def signup(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    if request.method == "POST":
        form = SignUpForm(request.POST, logged_in_user=None)
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
        if request.user.is_authenticated:
            messages.info(
                request,
                {
                    "title": "INFO: ",
                    "message_content": "You are already logged-in.",
                },
            )
            return render(
                request,
                "home/websitepage.html",
                {
                    "title": "Welcome!",
                    "website": website,
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                },
            )
        else:
            form = SignUpForm(logged_in_user=None)
    return render(
        request,
        "home/signup.html",
        {
            "form": form,
            "title": "Sign Up",
            "website": website,
        },
    )


def edit_profile(request, website_pk, website_name, profile_pk):
    website = get_object_or_404(Website, id=website_pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    elif profile_pk != request.user.id:
        messages.error(
            request,
            {
                "title": "ERROR: ",
                "message_content": "You don't have permission to edit this user.",
            },
        )
        return render(
            request,
            "home/websitepage.html",
            {
                "title": "Welcome!",
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
            },
        )
    else:
        if request.method == "GET":
            form = SignUpForm(instance=request.user, logged_in_user=request.user.id)
        else:
            form = SignUpForm(
                request.POST,
                request.FILES,
                instance=request.user,
                logged_in_user=request.user.id,
            )
            if form.is_valid():
                form.save()
                raw_password = form.cleaned_data.get("password1")
                user_name = form.cleaned_data.get("username")
                user = authenticate(username=user_name, password=raw_password)
                login(request, user)
                messages.success(
                    request,
                    {
                        "title": "SUCCESS: ",
                        "message_content": "Your profile has updated successfuly.",
                    },
                )
        return render(
            request,
            "home/edit_profile.html",
            {
                "form": form,
                "title": "Edit " + request.user.username + " Details",
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
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
            else:
                form = BusinessForm()
                return render(
                    request,
                    "home/new_business.html",
                    {
                        "form": form,
                        "title": "New Business",
                        "website": website,
                        "website_profile_pair": Website_Profile.get_website_profile_pair(
                            request.user, website
                        ),
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
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
            },
        )


def choose_business_to_edit(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        if request.method == "POST":
            chosen_business = Business.objects.get(id=request.POST.get("business", ""))
            return redirect(
                "edit_business", website.id, website.name, chosen_business.id
            )
        else:
            form = UserBusinessesForm(logged_in_user=request.user.id)
            return render(
                request,
                "home/choose_object_to_edit.html",
                {
                    "title": "Edit business",
                    "form": form,
                    "object": "business",
                    "website": website,
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                },
            )


def edit_business(request, website_pk, website_name, business_pk):
    website = get_object_or_404(Website, id=website_pk)
    business = get_object_or_404(Business, id=business_pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    elif business.profile.user.id != request.user.id:
        messages.error(
            request,
            {
                "title": "ERROR: ",
                "message_content": "You don't have permission to edit this business",
            },
        )
        return render(
            request,
            "home/websitepage.html",
            {
                "title": "Welcome!",
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
            },
        )
    else:
        if request.method == "GET":
            form = BusinessForm(instance=business)
        else:
            form = BusinessForm(request.POST, request.FILES, instance=business)
            if form.is_valid():
                form.save()
        return render(
            request,
            "home/edit_object.html",
            {
                "title": "Edit " + business.name,
                "business_name": business.name,
                "form": form,
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
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
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
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
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                },
            )
        else:
            return render(
                request,
                "home/premium.html",
                {
                    "title": "AG Premium",
                    "website": website,
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
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
                            "website_profile_pair": Website_Profile.get_website_profile_pair(
                                request.user, website
                            ),
                        },
                    )
            return render(
                request,
                "home/new_sale.html",
                {
                    "form": form,
                    "title": "New Sale",
                    "website": website,
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
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
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                },
            )


def choose_sale_to_edit(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        if request.method == "POST":
            chosen_sale = Sale.objects.get(id=request.POST.get("sale", ""))
            return redirect("edit_sale", website.id, website.name, chosen_sale.id)
        else:
            form = UserSalesForm(logged_in_user=request.user.id)
            return render(
                request,
                "home/choose_object_to_edit.html",
                {
                    "title": "Edit sale",
                    "form": form,
                    "object": "sale",
                    "website": website,
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                },
            )


def edit_sale(request, website_pk, website_name, sale_pk):
    website = get_object_or_404(Website, id=website_pk)
    sale = get_object_or_404(Sale, id=sale_pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    elif sale.profile.user.id != request.user.id:
        messages.error(
            request,
            {
                "title": "ERROR: ",
                "message_content": "You don't have permission to edit this sale",
            },
        )
        return render(
            request,
            "home/websitepage.html",
            {
                "title": "Welcome!",
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
            },
        )
    else:
        if request.method == "GET":
            form = SaleForm(instance=sale, logged_in_user=request.user.id)
        else:
            form = SaleForm(
                request.POST,
                request.FILES,
                instance=sale,
                logged_in_user=request.user.id,
            )
            if form.is_valid():
                form.save()
        return render(
            request,
            "home/edit_object.html",
            {
                "title": "Edit " + sale.title,
                "business_name": sale.title,
                "form": form,
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
            },
        )


def business_page(request, webpage_pk, website_name, business_pk, business_name):
    website = get_object_or_404(Website, id=webpage_pk)
    business = get_object_or_404(Business, id=business_pk)
    context = {
        "business": business,
        "website": website,
    }
    if request.user.is_authenticated:
        context["website_profile_pair"] = Website_Profile.get_website_profile_pair(
            request.user, website
        )
    return render(request, "home/business_page.html", context)


def login_view(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    form = AuthenticationForm()

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        website_profile_pair = Website_Profile.get_website_profile_pair(user, website)

        if (user is not None) and (website_profile_pair is not None):
            login(request, user)
            return redirect("websitepage", website.id, website.name)
        else:
            if user is None:
                message_content = "Invalid username/password."
            else:
                message_content = "This user is not connected to this website."
            messages.error(
                request,
                {
                    "title": "ERROR: ",
                    "message_content": message_content,
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
