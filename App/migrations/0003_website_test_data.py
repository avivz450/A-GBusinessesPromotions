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
                "#fff",
                "#4f5a62",
                "#3498db",
                "#fff",
                "#0009FF",
                21,
            ),
            (
                "Vegan",
                "App/images/WebsitesLogos/test_data/Vegan/Vegan_Logo.png",
                2,
                "#B5E63F",
                "#33A300",
                "#01FF42",
                "#B5E63F",
                "#33A300",
                21,
            ),
            (
                "Coffee",
                "App/images/WebsitesLogos/test_data/Coffee/Coffee_Logo.png",
                2,
                "#FF8601",
                "#583100",
                "#3498db",
                "#fff",
                "#FF8601",
                22,
            ),
            (
                "Electronics",
                "App/images/WebsitesLogos/test_data/Electronics/Electronics_Logo.png",
                2,
                "#fff",
                "#4f5a62",
                "#E4EA01",
                "#fff",
                "#E4EA01",
                22,
            ),
            (
                "Carnibors",
                "App/images/WebsitesLogos/test_data/Carnibors/Carnibors_Logo.png",
                2,
                "#fff",
                "#BA0102",
                "#FF0103",
                "#fff",
                "#BA0102",
                22,
            ),
            (
                "Candies",
                "App/images/WebsitesLogos/test_data/Candies/Candies_Logo.png",
                2,
                "#01E8E6",
                "#FF01C6",
                "#FF017A",
                "#FF01C6",
                "#01E8E6",
                22,
            ),
            (
                "Fitness",
                "App/images/WebsitesLogos/test_data/Fitness/Fitness_Logo.png",
                3,
                "#fff",
                "#41EE5C",
                "#7AFF01",
                "#fff",
                "#41EE5C",
                22,
            ),
            (
                "Craftig",
                "App/images/WebsitesLogos/test_data/Crafting/Crafting_Logo.png",
                2,
                "#fff",
                "#EB01FF",
                "#FF01B5",
                "#fff",
                "#EB01FF",
                22,
            ),
            (
                "Dairy",
                "App/images/WebsitesLogos/test_data/Dairy/Dairy_Logo.png",
                2,
                "##FEFFC8",
                "#4f5a62",
                "#3498db",
                "#fff",
                "#0009FF",
                22,
            ),
        ]

        with transaction.atomic():
            for (
                website_name,
                logo,
                number_of_slides,
                navbar_background_color,
                navbar_text_color,
                navbar_hover_text_color,
                sliders_text_color,
                sliders_carsoul_color,
                user,
            ) in website_test_data:
                website = Website(
                    name=website_name,
                    logo=logo,
                    number_of_slides_in_main_page=number_of_slides,
                    navbar_background_color=navbar_background_color,
                    navbar_text_color=navbar_text_color,
                    navbar_hover_text_color=navbar_hover_text_color,
                    sliders_text_color=sliders_text_color,
                    sliders_carsoul_color=sliders_carsoul_color,
                )
                website.save()
                profile = get_object_or_404(Profile, pk=user)

                profile.match_website_to_profile(website)

    operations = [
        migrations.RunPython(generate_data),
    ]
