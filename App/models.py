from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    '''
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
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    is_blocked = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return '{self.user.username}'.format(self=self)


class Business(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True, upload_to=None)
    URL = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    facebook_link = models.TextField(null=True, blank=True)
    instagram_link = models.TextField(null=True, blank=True)
    picture_0 = models.ImageField(null=True, blank=True, upload_to=None)
    picture_1 = models.ImageField(null=True, blank=True, upload_to=None)
    picture_2 = models.ImageField(null=True, blank=True, upload_to=None)
    from_hour = models.TimeField(default=None)
    to_hour = models.TimeField(default=None)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    is_confirmed = models.BooleanField(default=False)
