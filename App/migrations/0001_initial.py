# Generated by Django 3.2.5 on 2021-07-20 02:18

import ckeditor.fields
import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Business",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "logo",
                    models.ImageField(
                        default=None, upload_to="App/images/BusinessesLogos/"
                    ),
                ),
                ("description", ckeditor.fields.RichTextField(default=None)),
                ("URL", models.URLField(blank=True, max_length=250, null=True)),
                (
                    "facebook_link",
                    models.URLField(blank=True, max_length=250, null=True),
                ),
                (
                    "instagram_link",
                    models.URLField(blank=True, max_length=250, null=True),
                ),
                (
                    "picture_0",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="App/images/BusinessesPictures/",
                    ),
                ),
                (
                    "picture_1",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="App/images/BusinessesPictures/",
                    ),
                ),
                (
                    "picture_2",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="App/images/BusinessesPictures/",
                    ),
                ),
                ("from_hour", models.TimeField(blank=True, null=True)),
                ("to_hour", models.TimeField(blank=True, null=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(
                        blank=True, max_length=63, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=80)),
                ("message", ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="auth.user",
                    ),
                ),
                ("is_blocked", models.BooleanField(default=False)),
                ("is_vip", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Website",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "favicon",
                    models.ImageField(
                        default="App/images/WebsitesLogos/default.jpg",
                        upload_to="App/images/WebsitesLogos/",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        default="App/images/WebsitesLogos/default.jpg",
                        upload_to="App/images/WebsitesLogos/",
                    ),
                ),
                (
                    "number_of_slides_in_main_page",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(3),
                        ],
                    ),
                ),
                (
                    "navbar_background_color",
                    colorfield.fields.ColorField(default="#fff", max_length=18),
                ),
                (
                    "navbar_text_color",
                    colorfield.fields.ColorField(default="#4f5a62", max_length=18),
                ),
                (
                    "navbar_hover_text_color",
                    colorfield.fields.ColorField(default="#3498db", max_length=18),
                ),
                (
                    "sliders_text_color",
                    colorfield.fields.ColorField(default="#fff", max_length=18),
                ),
                (
                    "sliders_carsoul_color",
                    colorfield.fields.ColorField(default="#blue", max_length=18),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Website_Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wp_profile_ID",
                        to="App.profile",
                    ),
                ),
                (
                    "website",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="website_ID",
                        to="App.website",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Website_Business",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_confirmed",
                    models.CharField(
                        choices=[
                            ("AP", "Approved"),
                            ("DA", "Disapproved"),
                            ("PD", "Pending"),
                        ],
                        default="PD",
                        max_length=2,
                    ),
                ),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="business_ID",
                        to="App.business",
                    ),
                ),
                (
                    "website",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wb_website_ID",
                        to="App.website",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="website",
            name="businesses",
            field=models.ManyToManyField(
                through="App.Website_Business", to="App.Business"
            ),
        ),
        migrations.AddField(
            model_name="website",
            name="profiles",
            field=models.ManyToManyField(
                through="App.Website_Profile", to="App.Profile"
            ),
        ),
        migrations.CreateModel(
            name="Slide",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "picture",
                    models.ImageField(
                        default=None, upload_to="App/images/SlidePictures/"
                    ),
                ),
                ("description", models.TextField(default=None, max_length=500)),
                (
                    "website",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App.website"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                (
                    "picture",
                    models.ImageField(
                        default=None, upload_to="App/images/SalesPictures/"
                    ),
                ),
                ("description", models.TextField(default=None, max_length=50)),
                (
                    "is_confirmed",
                    models.CharField(
                        choices=[
                            ("AP", "Approved"),
                            ("DA", "Disapproved"),
                            ("PD", "Pending"),
                        ],
                        default="PD",
                        max_length=2,
                    ),
                ),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App.business"
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App.profile"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="websites",
            field=models.ManyToManyField(
                through="App.Website_Profile", to="App.Website"
            ),
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("notification_type", models.IntegerField(default=None)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                ("user_has_seen", models.BooleanField(default=False)),
                (
                    "from_user",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notification_from",
                        to="App.profile",
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notification_to",
                        to="App.profile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="business",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="App.profile"
            ),
        ),
        migrations.AddField(
            model_name="business",
            name="websites",
            field=models.ManyToManyField(
                through="App.Website_Business", to="App.Website"
            ),
        ),
        migrations.AddConstraint(
            model_name="website_profile",
            constraint=models.UniqueConstraint(
                fields=("profile", "website"), name="profile_website"
            ),
        ),
        migrations.AddConstraint(
            model_name="website_business",
            constraint=models.UniqueConstraint(
                fields=("website", "business"), name="website_business"
            ),
        ),
    ]
