from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business, Sale, Website, Website_Business, Profile, Slide, Contact


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        logged_in_user = kwargs.pop("logged_in_user", None)
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.logged_in_user = None
        if logged_in_user:
            self.logged_in_user = logged_in_user

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if self.logged_in_user:
            num_of_users_with_inserted_email = (
                User.objects.filter(email=email).exclude(id=self.logged_in_user).count()
            )
        else:
            num_of_users_with_inserted_email = User.objects.filter(email=email).count()

        if email and num_of_users_with_inserted_email > 0:
            raise forms.ValidationError(
                "This email address is already in use. Please supply a different email address."
            )
        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = (
            "name",
            "logo",
            "URL",
            "from_hour",
            "to_hour",
            "phone_number",
            "picture_0",
            "picture_1",
            "picture_2",
            "facebook_link",
            "instagram_link",
            "location",
            "location_points",
            "description",
        )


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = (
            "name",
            "logo",
            "favicon",
            "number_of_slides_in_main_page",
            "navbar_background_color",
            "navbar_text_color",
            "navbar_hover_text_color",
            "sliders_text_color",
            "sliders_carsoul_color",
        )


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = (
            "title",
            "description",
            "picture",
        )


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ("title", "business", "description", "picture")

    def __init__(self, *args, **kwargs):
        logged_in_user = kwargs.pop("logged_in_user", None)
        logged_in_profile = Profile.objects.filter(user=logged_in_user).first()
        website = kwargs.pop("website", None)
        super(SaleForm, self).__init__(*args, **kwargs)
        businesses = []

        for website_business_pair in Website_Business.objects.filter(
            website=website, is_confirmed=Website_Business.BusinessStatus.APPROVED
        ):
            if website_business_pair.business.profile == logged_in_profile:
                businesses.append(website_business_pair.business.id)

        self.fields["business"].queryset = Business.objects.filter(id__in=businesses)


class ChooseWebsiteForm(forms.Form):
    website = forms.ModelMultipleChoiceField(
        queryset=Website.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "selectpicker",
                "data-live-search": "true",
                "data-show-subtext": "true",
            }
        ),
    )


class UserSalesForm(forms.Form):
    sale = forms.ModelMultipleChoiceField(queryset=Sale.objects.all())

    def __init__(self, *args, **kwargs):
        logged_in_user = kwargs.pop("logged_in_user", None)
        super(UserSalesForm, self).__init__(*args, **kwargs)
        self.fields["sale"].queryset = Sale.objects.filter(
            profile=logged_in_user, is_confirmed=Sale.SaleStatus.APPROVED
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "full_name",
            "email",
            "subject",
            "message",
        )
