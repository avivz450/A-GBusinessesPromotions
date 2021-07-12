from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0015_auto_20210712_1210"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Website, Profile
        from django.shortcuts import get_object_or_404

        website_test_data = [
            (
                "Website Demo",
                "App/images/WebsitesLogos/test_data/Website_Demo/AG_Logo.png",
                2,
            ),
            ("Vegan", "App/images/WebsitesLogos/test_data/Vegan/Vegan_Logo.png", 2),
        ]

        with transaction.atomic():
            for website_name, logo, number_of_slides in website_test_data:
                website = Website(
                    name=website_name,
                    logo=logo,
                    number_of_slides_in_main_page=number_of_slides,
                )
                website.save()
                profile = get_object_or_404(Profile, pk=4)
                profile.match_website_to_profile(website)

    operations = [
        migrations.RunPython(generate_data),
    ]
