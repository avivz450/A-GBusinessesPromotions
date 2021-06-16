from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField


# Create your models here.
class Profile(models.Model):
    """
    Profile will be used as the base user in the Shlifim website.
    Profile is an extention to the imported 'User' from 'django.contrib.auth.models'.
    Imported Fields:
    username - Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.
    password - Required. A hash of, and metadata about, the password. (Django doesn’t store the raw password).
               Raw passwords can be arbitrarily long and can contain any character.
    date_joined - A datetime designating when the account was created. Is set to the current date/time by default
        when the account is created.
    email - Email address.
    is_superuser - Boolean. Designates that this user has all permissions without explicitly assigning them.
    Added Fields:
    is blocked - Boolean. Designates that this user won't be able to login until an admin unblockes him.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    is_blocked = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return "{self.user.username}".format(self=self)


class Business(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # required
    name = models.CharField(max_length=30)  # required
    logo = models.ImageField(
        default=None, upload_to="App/images/BusinessesLogos/"
    )  # required
    description = RichTextField(default=None)  # required
    URL = models.URLField(null=True, blank=True, max_length=250)
    facebook_link = models.URLField(null=True, blank=True, max_length=250)
    instagram_link = models.URLField(null=True, blank=True, max_length=250)
    picture_0 = models.ImageField(
        null=True, blank=True, upload_to="App/images/BusinessesPictures/"
    )
    picture_1 = models.ImageField(
        null=True, blank=True, upload_to="App/images/BusinessesPictures/"
    )
    picture_2 = models.ImageField(
        null=True, blank=True, upload_to="App/images/BusinessesPictures/"
    )
    from_hour = models.TimeField(
        null=True, blank=True, auto_now=False, auto_now_add=False
    )
    to_hour = models.TimeField(
        null=True, blank=True, auto_now=False, auto_now_add=False
    )
    phone_number = PhoneNumberField(null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return "{self.name}".format(self=self)


class Sale(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # required
    business = models.ForeignKey(Business, on_delete=models.CASCADE)  # required
    title = models.CharField(max_length=30)
    picture = models.ImageField(
        default=None,
        upload_to="App/images/SalesPictures/",
    )
    description = models.TextField(
        default=None, max_length=50
    )  # To Do : limit description length
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return "{self.title}".format(self=self)


class Notification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(default=None)  # To Do : limit description length

    def __str__(self):
        return "{self.user.username}".format(self=self)


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=80)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return "{self.name}".format(self=self)
