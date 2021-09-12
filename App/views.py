from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from .models import (
    Sale,
    Profile,
    Business,
    Website,
    Website_Profile,
    Website_Business,
    Slide,
    Notification,
    Business_Category,
    Business_Image,
)
from .forms import (
    SignUpForm,
    BusinessForm,
    SaleForm,
    ChooseWebsiteForm,
    WebsiteForm,
    SlideForm,
    ContactForm,
    BusinessCategoryForm,
    UserCategoryForm,
    BusinessImageForm,
)
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def websitepage(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    slideList = Slide.objects.filter(website=website)
    is_profile_admin = False
    context = {
        "website": website,
        "slideList": slideList,
    }
    if request.user.is_authenticated:
        website_profile_pair = Website_Profile.get_website_profile_pair(
            request.user, website
        )
        if website_profile_pair is None:
            logout(request)
        else:
            context["website_profile_pair"] = website_profile_pair
            context["is_profile_admin"] = True

    return render(request, "home/websitepage.html", context)


def landingpage(request):
    return render(
        request,
        "home/landingpage.html",
        {"title": "Welcome!"},
    )


def choose_website(request):
    choose_website_form = ChooseWebsiteForm()

    if request.method == "POST":
        if request.POST.get("transfer_to_website_button") == "submitted":
            choose_website_form = ChooseWebsiteForm(request.POST)
            selected_website_id = request.POST.get("website")
            selected_website = Website.objects.filter(id=selected_website_id).first()
            return redirect("websitepage", selected_website.id, selected_website.name)

    return render(
        request,
        "home/choose_website.html",
        {
            "title": "Welcome!",
            "choose_website_form": choose_website_form,
        },
    )


def landingpage_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, logged_in_user=None)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user.save()
            profile = Profile(user=user)
            user = authenticate(username=user.username, password=raw_password)
            profile.save()
            login(request, user)
            return redirect("add_website")
    else:
        form = SignUpForm(logged_in_user=None)
    return render(
        request,
        "home/landinpage_signup.html",
        {
            "form": form,
            "title": "Sign Up",
        },
    )


@login_required(login_url="/login/")
def add_website(request):
    if request.method == "POST":
        form = WebsiteForm(request.POST, request.FILES)
        if form.is_valid():
            new_website = form.save()
            return redirect(
                "add_categories",
                new_website.id,
                new_website.number_of_businesses_categories,
                new_website.number_of_slides_in_main_page,
            )
    else:
        form = WebsiteForm()
    return render(
        request,
        "home/add_website.html",
        {
            "form": form,
            "title": "Add Website",
        },
    )


@login_required(login_url="/login/")
def add_categories(
    request, new_website_id, number_of_categories_to_submit, number_of_slides_to_submit
):
    website = get_object_or_404(Website, id=new_website_id)
    category_form_list = []

    if request.method == "POST":
        for i in range(number_of_categories_to_submit):
            curr_business_category_form = BusinessCategoryForm(
                request.POST, prefix="caregory_form_" + str(i)
            )
            if curr_business_category_form.is_valid():
                curr_business_category = curr_business_category_form.save(commit=False)
                curr_business_category.website = website
                curr_business_category.save()
        return redirect("add_slides", new_website_id, number_of_slides_to_submit)
    else:
        for i in range(number_of_categories_to_submit):
            category_form_list.append(
                BusinessCategoryForm(prefix="caregory_form_" + str(i))
            )
        return render(
            request,
            "home/add_categories.html",
            {
                "category_form_list": category_form_list,
                "website": website,
                "title": "Add Categories",
            },
        )


@login_required(login_url="/login/")
def add_slides(request, new_website_id, number_of_slides_to_submit):
    website = get_object_or_404(Website, id=new_website_id)
    slide_form_list = []
    if request.method == "POST":
        for i in range(number_of_slides_to_submit):
            curr_slide_form = SlideForm(
                request.POST, request.FILES, prefix="slide_form_" + str(i)
            )
            if curr_slide_form.is_valid():
                curr_slide = curr_slide_form.save(commit=False)
                curr_slide.website = website
                curr_slide.save()
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.create(
            profile=logged_in_profile, website=website, is_admin=True
        )
        website_profile_pair.save()
        messages.success(
            request,
            {
                "title": "SUCCESS: ",
                "message_content": "Your website has been created successfuly!",
            },
        )
        slideList = Slide.objects.filter(website=website)
        return render(
            request,
            "home/websitepage.html",
            {
                "title": "Add Slides to website",
                "website": website,
                "website_profile_pair": website_profile_pair,
                "slideList": slideList,
            },
        )
    else:
        for i in range(number_of_slides_to_submit):
            slide_form_list.append(SlideForm(prefix="slide_form_" + str(i)))
        return render(
            request,
            "home/add_slides.html",
            {
                "slide_form_list": slide_form_list,
                "website": website,
                "title": "Add Slide to " + website.name,
            },
        )


def businesses(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    category_website_business_dictionary = {}
    website_business_pairs = Website_Business.objects.filter(
        website=website, is_confirmed=Website_Business.BusinessStatus.APPROVED
    )

    for website_business_pair in website_business_pairs:
        if website_business_pair.category_name in category_website_business_dictionary:
            category_website_business_dictionary[
                website_business_pair.category_name
            ].append(website_business_pair)
        else:
            category_website_business_dictionary[
                website_business_pair.category_name
            ] = [website_business_pair]

    context = {
        "website_business_pairs": Website_Business.objects.filter(
            website=website, is_confirmed=Website_Business.BusinessStatus.APPROVED
        ),
        "website": website,
        "category_website_business_dictionary_keys": category_website_business_dictionary.items(),
        "category_website_business_dictionary": category_website_business_dictionary.values(),
    }

    if request.user.is_authenticated:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
        context["website_profile_pair"] = Website_Profile.get_website_profile_pair(
            request.user, website
        )

    return render(request, "home/businesses.html", context)


def sales(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    sales = website.get_website_approved_sales()
    context = {
        "sales": sales,
        "website": website,
    }

    if request.user.is_authenticated:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
        context["website_profile_pair"] = Website_Profile.get_website_profile_pair(
            request.user, website
        )
    if request.method == "POST":
        filterText = request.POST.get("search", "")
        filteredSales = [
            sale for sale in sales if filterText.lower() in sale.title.lower()
        ]
        context["sales"] = filteredSales

    return render(request, "home/sales.html", context)


def signup(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    is_profile_admin = False
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
            logged_in_profile = Profile.objects.filter(user=request.user).first()
            website_profile_pair = Website_Profile.objects.filter(
                profile=logged_in_profile, is_admin=True
            )
            if website_profile_pair:
                is_profile_admin = True
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
                    "slideList": Slide.objects.filter(website=website),
                    "is_profile_admin": is_profile_admin,
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
            "is_profile_admin": is_profile_admin,
        },
    )


def edit_profile(request, website_pk, website_name, profile_pk):
    website = get_object_or_404(Website, id=website_pk)
    context = {}

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
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        context = {
            "title": "Welcome!",
            "website": website,
            "website_profile_pair": Website_Profile.get_website_profile_pair(
                request.user, website
            ),
            "slideList": Slide.objects.filter(website=website),
        }
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
        return render(
            request,
            "home/websitepage.html",
            context,
        )
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
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
        context = {
            "form": form,
            "title": "Edit " + request.user.username + " Details",
            "website": website,
            "website_profile_pair": Website_Profile.get_website_profile_pair(
                request.user, website
            ),
        }
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
        return render(request, "home/edit_profile.html", context)


def new_business(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    is_profile_admin = False

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        num_of_businesses_of_profile = len(
            Business.objects.filter(profile=logged_in_profile)
        )
        if logged_in_profile.is_vip or num_of_businesses_of_profile == 0:
            if request.method == "POST":
                category_form = UserCategoryForm(request.POST, website=website)
                business_form = BusinessForm(request.POST, request.FILES)
                if business_form.is_valid() and category_form.is_valid():
                    new_business = business_form.save(commit=False)
                    new_business.profile = logged_in_profile
                    new_business.save()
                    business_category = Business_Category.objects.filter(
                        id=request.POST.get("business_category", "")
                    ).first()
                    website.match_business_to_website(
                        new_business,
                        Website_Business.BusinessStatus.PENDING,
                        business_category.category_name,
                    )
                    return redirect(
                        "business_additional_pictures",
                        website.id,
                        website.name,
                        new_business.id,
                        new_business.name,
                        new_business.number_of_additional_pictures,
                    )
            else:
                category_form = UserCategoryForm(website=website)
                business_form = BusinessForm()
                return render(
                    request,
                    "home/new_business.html",
                    {
                        "business_form": business_form,
                        "category_form": category_form,
                        "title": "New Business",
                        "website": website,
                        "website_profile_pair": Website_Profile.get_website_profile_pair(
                            request.user, website
                        ),
                        "is_profile_admin": is_profile_admin,
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
                "slideList": Slide.objects.filter(website=website),
                "is_profile_admin": is_profile_admin,
            },
        )


def business_additional_pictures(
    request, webpage_pk, website_name, business_pk, business_name, additional_pictures
):
    website = get_object_or_404(Website, id=webpage_pk)
    business = get_object_or_404(Business, id=business_pk)
    image_form_list = []

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        is_profile_admin = False
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        if request.method == "POST":
            for i in range(additional_pictures):
                curr_business_image_form = BusinessImageForm(
                    request.POST, request.FILES, prefix="image_form_" + str(i)
                )
                if curr_business_image_form.is_valid():
                    curr_business_image = curr_business_image_form.save(commit=False)
                    curr_business_image.business = business
                    curr_business_image.save()
            msg_content = """The business was successfully inserted.
                    It will be visible once the site administrators will approve it."""
            messages.info(
                request,
                {
                    "title": "INFO: ",
                    "message_content": msg_content,
                },
            )
            website_admin_set = Website_Profile.objects.filter(
                website=website, is_admin=True
            )
            for website_profile_instance in website_admin_set:
                notification = Notification.objects.create(
                    notification_type=2,
                    from_user=logged_in_profile,
                    to_user=website_profile_instance.profile,
                )
                notification.save()
            return render(
                request,
                "home/websitepage.html",
                {
                    "title": "Welcome!",
                    "website": website,
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                    "slideList": Slide.objects.filter(website=website),
                    "is_profile_admin": True,
                },
            )
        else:
            for i in range(additional_pictures):
                image_form_list.append(BusinessImageForm(prefix="image_form_" + str(i)))
            return render(
                request,
                "home/add_images.html",
                {
                    "image_form_list": image_form_list,
                    "website": website,
                    "business": business,
                    "title": "Add Business Images",
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                    "is_profile_admin": is_profile_admin,
                },
            )


def edit_business(request, website_pk, website_name, business_pk):
    website = get_object_or_404(Website, id=website_pk)
    business = get_object_or_404(Business, id=business_pk)
    is_profile_admin = False
    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    elif business.profile.user.id != request.user.id:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
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
                "slideList": Slide.objects.filter(website=website),
                "is_profile_admin": is_profile_admin,
            },
        )
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        if request.method == "GET":
            form = BusinessForm(instance=business)
        else:
            form = BusinessForm(request.POST, request.FILES, instance=business)
            if form.is_valid():
                form.save()
        return render(
            request,
            "home/edit_business.html",
            {
                "title": "Edit " + business.name,
                "business_name": business.name,
                "form": form,
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
                "is_profile_admin": is_profile_admin,
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
                    "slideList": Slide.objects.filter(website=website),
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
                    "slideList": Slide.objects.filter(website=website),
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
    is_profile_admin = False
    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        num_of_sales_of_profile = len(Sale.objects.filter(profile=logged_in_profile))

        if logged_in_profile.is_vip or num_of_sales_of_profile == 0:
            form = SaleForm(logged_in_user=request.user.id, website=website)
            if request.method == "POST":
                saleForm = SaleForm(
                    request.POST,
                    request.FILES,
                    logged_in_user=request.user.id,
                    website=website,
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
                    website_admin_set = Website_Profile.objects.filter(
                        website=website, is_admin=True
                    )
                    for website_profile_instance in website_admin_set:
                        notification = Notification.objects.create(
                            notification_type=4,
                            from_user=logged_in_profile,
                            to_user=website_profile_instance.profile,
                        )
                        notification.save()
                    return render(
                        request,
                        "home/websitepage.html",
                        {
                            "title": "Welcome!",
                            "website": website,
                            "website_profile_pair": Website_Profile.get_website_profile_pair(
                                request.user, website
                            ),
                            "slideList": Slide.objects.filter(website=website),
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
                    "is_profile_admin": is_profile_admin,
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
                    "slideList": Slide.objects.filter(website=website),
                    "is_profile_admin": is_profile_admin,
                },
            )


def edit_sale(request, website_pk, website_name, sale_pk):
    website = get_object_or_404(Website, id=website_pk)
    sale = get_object_or_404(Sale, id=sale_pk)
    is_profile_admin = False

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    elif sale.profile.user.id != request.user.id:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
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
                "slideList": Slide.objects.filter(website=website),
                "is_profile_admin": is_profile_admin,
            },
        )
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        if request.method == "GET":
            form = SaleForm(
                instance=sale, logged_in_user=request.user.id, website=website
            )
        else:
            form = SaleForm(
                request.POST,
                request.FILES,
                instance=sale,
                logged_in_user=request.user.id,
                website=website,
            )
            if form.is_valid():
                form.save()
        return render(
            request,
            "home/edit_sale.html",
            {
                "title": "Edit " + sale.title,
                "business_name": sale.title,
                "form": form,
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
                "is_profile_admin": is_profile_admin,
            },
        )


def business_page(request, webpage_pk, website_name, business_pk, business_name):
    is_profile_admin = False
    website_business_pair = Website_Business.objects.filter(
        website=webpage_pk, business=business_pk
    ).first()
    business_location_points = website_business_pair.business.location_points.split(",")
    business_images = Business_Image.objects.filter(
        business=website_business_pair.business
    )
    sales = Sale.objects.filter(business=business_pk)
    context = {
        "business": website_business_pair.business,
        "website": website_business_pair.website,
        "latitude": business_location_points[0],
        "longitude": business_location_points[1],
        "website_business_pair": website_business_pair,
        "business_images": business_images,
        "sales": sales,
        "is_profile_admin": is_profile_admin,
    }
    if request.user.is_authenticated:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            context["is_profile_admin"] = is_profile_admin
        context["website_profile_pair"] = Website_Profile.get_website_profile_pair(
            request.user, website_business_pair.website
        )
    return render(request, "home/business_page.html", context)


def login_view(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    form = AuthenticationForm()

    if request.POST.get("continue_button") == "Continue":
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
                messages.error(
                    request,
                    {
                        "title": "ERROR: ",
                        "message_content": message_content,
                    },
                )
            else:
                form = None
                request.session["user"] = user.id
    elif request.POST.get("connect_button") == "Connect":
        logged_in_profile = Profile.objects.filter(user=request.session["user"]).first()
        logged_in_profile.match_website_to_profile(website)
        login(request, logged_in_profile.user)
        return redirect("websitepage", website.id, website.name)

    return render(
        request,
        "home/login.html",
        {
            "website": website,
            "form": form,
        },
    )


class RemoveNotification(View):
    def delete(self, *args, **kwargs):
        notification = Notification.objects.get(pk=kwargs["notification_pk"])

        notification.user_has_seen = True
        notification.save()

        return HttpResponse("Success", content_type="text/plain")


def admin_businesses(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    is_profile_admin = False
    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        return render(
            request,
            "home/admin_section/businesses.html",
            {
                "title": "Admin Section - Businesses",
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
                "website_business_pairs": Website_Business.objects.filter(
                    website=website
                ),
                "is_profile_admin": is_profile_admin,
            },
        )


def change_business_status(request, pk, website_name, business_id, business_new_status):
    website_business_pair = get_object_or_404(Website_Business, id=business_id)
    logged_in_profile = Profile.objects.filter(user=request.user).first()
    profile_to_send_notification = website_business_pair.business.profile

    if business_new_status == "AP":
        website_business_pair.is_confirmed = Website_Business.BusinessStatus.APPROVED
        notification = Notification.objects.create(
            notification_type=1,
            from_user=logged_in_profile,
            to_user=profile_to_send_notification,
        )
        notification.save()
    else:
        website_business_pair.is_confirmed = Website_Business.BusinessStatus.DISAPPROVED
        notification = Notification.objects.create(
            notification_type=5,
            from_user=logged_in_profile,
            to_user=profile_to_send_notification,
        )
        notification.save()

    website_business_pair.save()

    return redirect("admin_businesses", pk, website_name)


def admin_sales(request, pk, website_name, activated_filter):
    website = get_object_or_404(Website, id=pk)
    is_profile_admin = False

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        website_business_pairs = Website_Business.objects.filter(website=website)
        related_sales_to_website = []

        for website_business_pair in website_business_pairs:
            if activated_filter == "Approved":
                related_sales_to_business = Sale.objects.filter(
                    business=website_business_pair.business,
                    is_confirmed=Sale.SaleStatus.APPROVED,
                )
            elif activated_filter == "Disapproved":
                related_sales_to_business = Sale.objects.filter(
                    business=website_business_pair.business,
                    is_confirmed=Sale.SaleStatus.DISAPPROVED,
                )
            elif activated_filter == "Pending":
                related_sales_to_business = Sale.objects.filter(
                    business=website_business_pair.business,
                    is_confirmed=Sale.SaleStatus.PENDING,
                )
            elif activated_filter == "All":
                related_sales_to_business = Sale.objects.filter(
                    business=website_business_pair.business
                )
            for sale in related_sales_to_business:
                related_sales_to_website.append(sale)

        return render(
            request,
            "home/admin_section/sales.html",
            {
                "title": "Admin Section - Sales",
                "website": website,
                "website_profile_pair": Website_Profile.get_website_profile_pair(
                    request.user, website
                ),
                "sales": related_sales_to_website,
                "activated_filter": activated_filter,
                "is_profile_admin": is_profile_admin,
            },
        )


def change_sale_status(
    request, pk, website_name, sale_id, sale_new_status, activated_filter
):
    sale = get_object_or_404(Sale, id=sale_id)
    logged_in_profile = Profile.objects.filter(user=request.user).first()
    profile_to_send_notification = sale.profile

    if sale_new_status == "AP":
        sale.is_confirmed = Sale.SaleStatus.APPROVED
        notification = Notification.objects.create(
            notification_type=3,
            from_user=logged_in_profile,
            to_user=profile_to_send_notification,
        )
        notification.save()
    else:
        sale.is_confirmed = Sale.SaleStatus.DISAPPROVED
        notification = Notification.objects.create(
            notification_type=6,
            from_user=logged_in_profile,
            to_user=profile_to_send_notification,
        )
        notification.save()

    sale.save()

    return redirect("admin_sales", pk, website_name, activated_filter)


def connect_businesses_page(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        website_business_pairs = Website_Business.objects.exclude(
            website=website
        ).order_by("website")
        user_website_business_pairs = []
        websites_to_connect_from = []

        for website_business_pair in website_business_pairs:
            if (
                website_business_pair.business.profile.user == request.user
                and website_business_pair.website not in websites_to_connect_from
                and len(
                    Website_Business.objects.filter(
                        business=website_business_pair.business, website=website
                    )
                )
                == 0
            ):
                websites_to_connect_from.append(website_business_pair.website)

        for website_with_user_businesses in websites_to_connect_from:
            for website_business_pair in Website_Business.objects.filter(
                website=website_with_user_businesses
            ):
                number_of_occurences_in_website = Website_Business.objects.filter(
                    website=website, business=website_business_pair.business
                )
                if (
                    website_business_pair.business.profile.user == request.user
                    and len(number_of_occurences_in_website) == 0
                ):
                    user_website_business_pairs.append(website_business_pair)
        context = {
            "title": "Connect businesses",
            "website": website,
            "website_profile_pair": Website_Profile.get_website_profile_pair(
                request.user, website
            ),
            "user_website_business_pairs": user_website_business_pairs,
            "websites_to_connect_from": websites_to_connect_from,
        }
        if website_profile_pair:
            context["is_profile_admin"] = True
        return render(
            request,
            "home/connect_business.html",
            context,
        )


def connect_business(request, pk, website_name, business_pk):
    website = get_object_or_404(Website, id=pk)
    business_to_connect = get_object_or_404(Business, id=business_pk)
    is_profile_admin = False

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if website_profile_pair:
            is_profile_admin = True
        if request.method == "POST":
            category_form = UserCategoryForm(request.POST, website=website)
            business_category = Business_Category.objects.filter(
                id=request.POST.get("business_category", "")
            ).first()
            if category_form.is_valid():
                new_business_website_pair = Website_Business(
                    website=website,
                    business=business_to_connect,
                    is_confirmed=Website_Business.BusinessStatus.PENDING,
                    category_name=business_category.category_name,
                )
                new_business_website_pair.save()
                messages.info(
                    request,
                    {
                        "title": "INFO: ",
                        "message_content": "Connection request of '"
                        + business_to_connect.name
                        + "' to '"
                        + website.name
                        + """'
                            has been succesfuly sent to the website's admins to review.""",
                    },
                )
                website_admin_set = Website_Profile.objects.filter(
                    website=website, is_admin=True
                )
                logged_in_profile = Profile.objects.filter(user=request.user).first()
                for website_profile_instance in website_admin_set:
                    notification = Notification.objects.create(
                        notification_type=2,
                        from_user=logged_in_profile,
                        to_user=website_profile_instance.profile,
                    )
                    notification.save()
                return render(
                    request,
                    "home/websitepage.html",
                    {
                        "title": "Welcome!",
                        "website": website,
                        "website_profile_pair": Website_Profile.get_website_profile_pair(
                            request.user, website
                        ),
                        "slideList": Slide.objects.filter(website=website),
                        "is_profile_admin": is_profile_admin,
                    },
                )
        else:
            category_form = UserCategoryForm(website=website)
            return render(
                request,
                "home/connected_business_category.html",
                {
                    "title": "Welcome!",
                    "website": website,
                    "business": business_to_connect,
                    "website_profile_pair": Website_Profile.get_website_profile_pair(
                        request.user, website
                    ),
                    "form": category_form,
                },
            )


def my_businesses(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    website_businesses_pair = Website_Business.objects.all()
    user_website_businesses_pairs = []

    for website_business_pair in website_businesses_pair:
        if website_business_pair.business.profile.user == request.user:
            user_website_businesses_pairs.append(website_business_pair)

    user_websites_businesses_dictionary = {}
    for user_website_businesses_pair in user_website_businesses_pairs:
        if user_website_businesses_pair.website in user_websites_businesses_dictionary:
            user_websites_businesses_dictionary[
                user_website_businesses_pair.website
            ].append(user_website_businesses_pair)
        else:
            user_websites_businesses_dictionary[
                user_website_businesses_pair.website
            ] = [user_website_businesses_pair]

    user_website_stripwebsite_dictionary = {}
    for user_website in user_websites_businesses_dictionary:
        user_website_stripwebsite_dictionary[user_website] = user_website.name.replace(
            " ", ""
        )

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        context = {}
        context = {
            "title": "My businesses",
            "website": website,
            "website_profile_pair": website_profile_pair,
            "user_websites_businesses_dictionary_keys": user_website_stripwebsite_dictionary.items(),
            "user_websites_businesses_dictionary": user_websites_businesses_dictionary.values(),
            "business_enum": Website_Business.BusinessStatus.choices,
        }
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
        return render(
            request,
            "home/my_businesses.html",
            context,
        )


import pdb


def contact_us(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)
    context = {
        "website": website,
    }
    if request.method == "GET":
        form = ContactForm()
        context["form"] = form
    else:
        form = ContactForm(request.POST)
        context["form"] = form
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                website_admin_set = Website_Profile.objects.filter(
                    website=website, is_admin=True
                )
                for website_profile_instance in website_admin_set:
                    send_mail(
                        full_name + " sent you a message from " + website_name,
                        "Subject: "
                        + subject
                        + "\n\n"
                        + "Message: "
                        + message
                        + "\n\n"
                        + "Email: "
                        + email,
                        email,
                        [website_profile_instance.profile.user.email],
                    )
                messages.success(
                    request,
                    {
                        "title": "SUCCESS: ",
                        "message_content": " Your message has been sent!",
                    },
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
    if request.user.is_authenticated:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
    return render(request, "home/contact_us.html", context)


def successView(request):
    return HttpResponse("Success! Thank you for your message.")


def my_malls(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        admin_website_profile_pairs = Website_Profile.objects.filter(
            profile=logged_in_profile
        )
        context = {
            "website": website,
            "website_profile_pair": Website_Profile.get_website_profile_pair(
                request.user, website
            ),
            "admin_website_profile_pairs": admin_website_profile_pairs,
        }
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True

    return render(request, "home/my_malls.html", context)


import pdb


def edit_mall(request, website_pk, website_name, mall_pk):
    website = get_object_or_404(Website, id=website_pk)
    mall_to_edit = get_object_or_404(Website, id=mall_pk)
    context = {}

    if request.user.is_authenticated:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True, website=website
        )

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    elif not website_profile_pair:
        messages.error(
            request,
            {
                "title": "ERROR: ",
                "message_content": "You don't have permission to edit this mall.",
            },
        )
        context = {
            "title": "Welcome!",
            "website": website,
            "website_profile_pair": Website_Profile.get_website_profile_pair(
                request.user, website
            ),
            "slideList": Slide.objects.filter(website=website),
        }
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
        return render(
            request,
            "home/websitepage.html",
            context,
        )
    else:
        if request.method == "GET":
            form = WebsiteForm(instance=mall_to_edit)
        else:
            form = WebsiteForm(
                request.POST,
                request.FILES,
                instance=mall_to_edit,
            )
            if form.is_valid():
                new_mall = form.save()
                messages.success(
                    request,
                    {
                        "title": "SUCCESS: ",
                        "message_content": mall_to_edit.name
                        + " has updated successfuly.",
                    },
                )
                slideList = Slide.objects.filter(website=website)
                context = {
                    "website": website,
                    "slideList": slideList,
                }
                if website_profile_pair:
                    context["is_profile_admin"] = True
                if new_mall.id == website.id:
                    context["website"] = new_mall
                return render(request, "home/websitepage.html", context)
        context = {
            "form": form,
            "title": "Edit " + mall_to_edit.name,
            "website": website,
            "website_profile_pair": Website_Profile.get_website_profile_pair(
                request.user, website
            ),
            "mall_to_edit": mall_to_edit,
        }
        if website_profile_pair:
            context["is_profile_admin"] = True

        return render(request, "home/edit_mall.html", context)


def my_sales(request, pk, website_name):
    website = get_object_or_404(Website, id=pk)

    if not request.user.is_authenticated:
        return redirect("login", website.id, website.name)
    else:
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, is_admin=True
        )
        logged_in_profile = Profile.objects.filter(user=request.user).first()
        sales = Sale.objects.filter(profile=logged_in_profile)
        context = {
            "sales": sales,
            "website": website,
            "website_profile_pair": Website_Profile.get_website_profile_pair(
                request.user, website
            ),
        }
        if not website_profile_pair:
            context["is_profile_admin"] = False
        else:
            context["is_profile_admin"] = True
        if request.method == "POST":
            filterText = request.POST.get("search", "")
            filteredSales = [
                sale for sale in sales if filterText.lower() in sale.title.lower()
            ]
            context["sales"] = filteredSales

    return render(request, "home/my_sales.html", context)
