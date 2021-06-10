from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business, Sale


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
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields["picture"].required = True
