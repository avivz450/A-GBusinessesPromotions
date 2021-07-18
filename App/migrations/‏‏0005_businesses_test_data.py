from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0004_slides_test_data"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Business, Profile, Website, Website_Business
        from django.shortcuts import get_object_or_404

        business_test_data = [
            (
                4,
                "Business demo 1",
                "App/images/BusinessesLogos/demo_business_1_logo.png",
                "Business demo 1 description",
                Website_Business.BusinessStatus.APPROVED,
                1,
            ),
            (
                4,
                "Business demo 2",
                "App/images/BusinessesLogos/demo_business_2_logo.png",
                "Business demo 2 description",
                Website_Business.BusinessStatus.PENDING,
                1,
            ),
            (
                4,
                "Business demo 3",
                "App/images/BusinessesLogos/demo_business_3_logo.png",
                "Business demo 3 description",
                Website_Business.BusinessStatus.APPROVED,
                1,
            ),
            (
                4,
                "MikiMaya",
                "App/images/BusinessesLogos/vegan_business_1_logo.jpg",
                "Mikimaya is a vegan restaurant in the town of Tzur Moshe, where you will find a menu rich in flavors.",
                Website_Business.BusinessStatus.APPROVED,
                2,
            ),
            (
                4,
                "BOCHI cafe",
                "App/images/BusinessesLogos/vegan_business_2_logo.jpg",
                """A house of veganism.
                Animal rehabilitation and ecology.
                At BOCHI cafe you can enjoy 100% vegan food, fair trade coffee and environmental protection.
                The special and magical thing about the cafe is that some of the proceeds go
                 directly to rescuing and rehabilitating animals!
                So for a powerful experience, donation and delicious food, do yourself a favor, visit BOCHI!""",
                Website_Business.BusinessStatus.PENDING,
                2,
            ),
            (
                4,
                "Magna Nature",
                "App/images/BusinessesLogos/vegan_business_3_logo.jpg",
                """"Magna Nature" is an online store for natural products that was
                 founded with the goal of providing a solution for people who prefer to use
                  products that are friendly to the body, mind and environment.
In the store you can find products that provide natural
 and healthy alternatives to the products consumed in your home.""",
                Website_Business.BusinessStatus.APPROVED,
                2,
            ),
        ]

        with transaction.atomic():
            for (
                profile_id,
                name,
                logo,
                description,
                is_confirmed,
                website_id,
            ) in business_test_data:
                website = Website.objects.filter(pk=website_id)[0]
                business = Business(
                    profile=get_object_or_404(Profile, pk=profile_id),
                    name=name,
                    logo=logo,
                    description=description,
                )
                business.save()
                website.match_business_to_website(business, is_confirmed)

    operations = [
        migrations.RunPython(generate_data),
    ]
