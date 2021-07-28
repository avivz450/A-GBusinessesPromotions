from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0002_user_test_data"),
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
            ("Coffee", "App/images/WebsitesLogos/test_data/Coffee/Coffee_Logo.png", 2),
            (
                "Electronics",
                "App/images/WebsitesLogos/test_data/Electronics/Electronics_Logo.png",
                2,
            ),
            (
                "Carnibors",
                "App/images/WebsitesLogos/test_data/Carnibors/Carnibors_Logo.png",
                2,
            ),
            (
                "Candies",
                "App/images/WebsitesLogos/test_data/Candies/Candies_Logo.png",
                2,
            ),
            (
                "Fitness",
                "App/images/WebsitesLogos/test_data/Fitness/Fitness_Logo.png",
                3,
            ),
            (
                "Craftig",
                "App/images/WebsitesLogos/test_data/Fitness/Crafting_Logo.png",
                2,
            ),
            ("Dairy", "App/images/WebsitesLogos/test_data/Dairy/Dairy_Logo.png", 2),
        ]

        with transaction.atomic():
            for website_name, logo, number_of_slides in website_test_data:
                website = Website(
                    name=website_name,
                    logo=logo,
                    number_of_slides_in_main_page=number_of_slides,
                )
                website.save()
                profile = get_object_or_404(Profile, pk=21)
                profile.match_website_to_profile(website)

    operations = [
        migrations.RunPython(generate_data),
    ]
