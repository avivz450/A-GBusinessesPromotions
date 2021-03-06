from django.conf import settings
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from location_field.models.plain import PlainLocationField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


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
    websites = models.ManyToManyField("Website", through="Website_Profile")

    def __str__(self):
        return "{self.user.username}".format(self=self)

    def match_website_to_profile(self, website, is_admin=False):
        website_profile_pair = Website_Profile()
        website_profile_pair.profile = self
        website_profile_pair.website = website
        website_profile_pair.is_admin = is_admin
        website_profile_pair.save()


class Website(models.Model):
    name = models.CharField(max_length=30)  # required
    favicon = models.ImageField(
        default="App/images/WebsitesLogos/default.jpg",
        upload_to="App/images/WebsitesLogos/",
    )
    logo = models.ImageField(
        default="App/images/WebsitesLogos/default.jpg",
        upload_to="App/images/WebsitesLogos/",
    )  # required
    number_of_slides_in_main_page = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    number_of_businesses_categories = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    profiles = models.ManyToManyField("Profile", through="Website_Profile")
    businesses = models.ManyToManyField("Business", through="Website_Business")
    navbar_background_color = ColorField(default="#fff")
    navbar_text_color = ColorField(default="#4f5a62")
    navbar_hover_text_color = ColorField(default="#3498db")
    sliders_text_color = ColorField(default="#fff")
    sliders_carsoul_color = ColorField(default="#0009FF")

    def __str__(self):
        return "{self.name}".format(self=self)

    def get_website_approved_sales(self):
        website_business_pairs = Website_Business.objects.filter(website=self)
        sales = []

        for website_business_pair in website_business_pairs:
            if website_business_pair.is_confirmed:
                for sale in Sale.objects.filter(
                    business=website_business_pair.business,
                    is_confirmed=Sale.SaleStatus.APPROVED,
                ):
                    sales.append(sale)

        return sales

    def match_business_to_website(self, business, is_confirmed, category_name):
        website_business_pair = Website_Business()
        website_business_pair.business = business
        website_business_pair.website = self
        website_business_pair.category_name = category_name
        website_business_pair.is_confirmed = is_confirmed
        website_business_pair.save()


class Business(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # required
    name = models.CharField(max_length=30)  # required
    logo = models.ImageField(
        default=None, upload_to="App/images/BusinessesLogos/"
    )  # required
    description = models.TextField(default=None)  # required
    URL = models.URLField(null=True, blank=True, max_length=250)
    facebook_link = models.URLField(null=True, blank=True, max_length=250)
    instagram_link = models.URLField(null=True, blank=True, max_length=250)
    youtube_link = models.URLField(null=True, blank=True, max_length=250)
    main_picture = models.ImageField(
        null=True, blank=True, upload_to="App/images/BusinessesPictures/"
    )
    location_image = models.ImageField(
        null=True, blank=True, upload_to="App/images/BusinessesPictures/"
    )
    number_of_additional_pictures = models.IntegerField(
        default=1, validators=[MinValueValidator(5), MaxValueValidator(10)]
    )
    hours = models.TextField(null=True, blank=True, max_length=300)
    phone_number = PhoneNumberField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    location_points = PlainLocationField(
        based_fields=["location"], zoom=7, null=True, blank=True
    )
    location_details = models.CharField(null=True, blank=True, max_length=100)
    websites = models.ManyToManyField("Website", through="Website_Business")

    def __str__(self):
        return "{self.name}".format(self=self)


class Business_Image(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="App/images/BusinessesPictures/")

    def __str__(self):
        return "{self.business.name}".format(self=self)


class Business_Category(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    category_name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return "{self.category_name}".format(self=self)


class Website_Business(models.Model):
    class BusinessStatus(models.TextChoices):
        APPROVED = "AP", _("Approved")
        DISAPPROVED = "DA", _("Disapproved")
        PENDING = "PD", _("Pending")

    website = models.ForeignKey(
        Website, on_delete=models.CASCADE, related_name="wb_website_ID"
    )
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="business_ID"
    )

    is_confirmed = models.CharField(
        max_length=2,
        choices=BusinessStatus.choices,
        default=BusinessStatus.PENDING,
    )
    category_name = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["website", "business"], name="website_business"
            )
        ]

    def __str__(self):
        return f"Website : {self.website}, business : {self.business}, "


class Slide(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)  # required
    title = models.CharField(max_length=200)  # required
    picture = models.ImageField(
        default=None,
        upload_to="App/images/SlidePictures/",
    )  # required
    description = models.TextField(default=None, max_length=500)  # required

    def __str__(self):
        return "{self.title}".format(self=self)


class Website_Profile(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="wp_profile_ID"
    )
    website = models.ForeignKey(
        Website, on_delete=models.CASCADE, related_name="website_ID"
    )
    is_admin = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "website"], name="profile_website"
            )
        ]

    def __str__(self):
        return f"User name : {self.profile}, Website : {self.website}"

    @classmethod
    def get_website_profile_pair(cls, user, website):
        logged_in_profile = Profile.objects.filter(user=user).first()
        website_profile_pair = Website_Profile.objects.filter(
            profile=logged_in_profile, website=website
        ).first()
        return website_profile_pair


class Sale(models.Model):
    class SaleStatus(models.TextChoices):
        APPROVED = "AP", _("Approved")
        DISAPPROVED = "DA", _("Disapproved")
        PENDING = "PD", _("Pending")

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
    is_confirmed = models.CharField(
        max_length=2,
        choices=SaleStatus.choices,
        default=SaleStatus.PENDING,
    )
    expired_date = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False
    )  # forms.DateTimeField(input_formats=["%m/%d/%Y %H:%M:%S"])

    def __str__(self):
        return "{self.title}".format(self=self)


class Notification(models.Model):
    # 1 = business approved, 2 = business request to add
    # 3 = sale approved, 4 = sale request to add
    # 5 = business disapproved, 6 = sale disapproved
    notification_type = models.IntegerField(default=None)
    to_user = models.ForeignKey(
        Profile,
        related_name="notification_to",
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    from_user = models.ForeignKey(
        Profile,
        related_name="notification_from",
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=80)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return "{self.name}".format(self=self)
