from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business, Sale, Website


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


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
            "description",
        )


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ("title", "business", "description", "picture")

    def __init__(self, *args, **kwargs):
        logged_in_user = kwargs.pop("logged_in_user", None)
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields["business"].queryset = Business.objects.filter(
            profile=logged_in_user
        )


class ChooseWebsiteForm(forms.Form):
    website = forms.ModelMultipleChoiceField(queryset=Website.objects.all())


class ChooseUserBusinessesForm(forms.Form):
    business = forms.ModelMultipleChoiceField(queryset=Business.objects.all())

    def __init__(self, *args, **kwargs):
        logged_in_user = kwargs.pop("logged_in_user", None)
        super(ChooseUserBusinessesForm, self).__init__(*args, **kwargs)
        self.fields["business"].queryset = Business.objects.filter(
            profile=logged_in_user
        )
