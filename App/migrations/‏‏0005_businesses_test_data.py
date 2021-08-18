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
                21,
                "Business demo 1",
                "App/images/BusinessesLogos/demo_business_1_logo.png",
                "Business demo 1 description",
                Website_Business.BusinessStatus.APPROVED,
                1,
                "demo",
            ),
            (
                21,
                "Business demo 2",
                "App/images/BusinessesLogos/demo_business_2_logo.png",
                "Business demo 2 description",
                Website_Business.BusinessStatus.PENDING,
                1,
                "demo",
            ),
            (
                21,
                "Business demo 3",
                "App/images/BusinessesLogos/demo_business_3_logo.png",
                "Business demo 3 description",
                Website_Business.BusinessStatus.APPROVED,
                1,
                "demo",
            ),
            (
                21,
                "MikiMaya",
                "App/images/BusinessesLogos/vegan_business_1_logo.jpg",
                "Mikimaya is a vegan restaurant in the town of Tzur Moshe, where you will find a menu rich in flavors.",
                Website_Business.BusinessStatus.APPROVED,
                2,
                "restaurant",
            ),
            (
                21,
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
                "restaurant",
            ),
            (
                21,
                "Magna Nature",
                "App/images/BusinessesLogos/vegan_business_3_logo.jpg",
                """"Magna Nature" is an online store for natural products that was
                 founded with the goal of providing a solution for people who prefer to use
                  products that are friendly to the body, mind and environment.
In the store you can find products that provide natural
 and healthy alternatives to the products consumed in your home.""",
                Website_Business.BusinessStatus.APPROVED,
                2,
                "food",
            ),
            (
                22,
                "Coffee Botique",
                "App/images/BusinessesLogos/coffee_lovers.jpg",
                """"Beans all over the world, to match the perfect taste to the
                every one...
                """,
                Website_Business.BusinessStatus.APPROVED,
                3,
                "food",
            ),
            (
                22,
                "Ninja",
                "App/images/BusinessesLogos/food_ninja.jpg",
                """"Electric kitchen machines.""",
                Website_Business.BusinessStatus.APPROVED,
                4,
                "store",
            ),
            (
                22,
                "The Big Butcher",
                "App/images/BusinessesLogos/food_butcher.jpg",
                """"Botique butcher with the most delicious meats.""",
                Website_Business.BusinessStatus.APPROVED,
                5,
                "food",
            ),
            (
                22,
                "Lets Go To The Candy Shop",
                "App/images/BusinessesLogos/food_candies.jpg",
                """"Candies candies and more candies, all kinds of candies in variety
                of flavors and colors.""",
                Website_Business.BusinessStatus.APPROVED,
                6,
                "food",
            ),
            (
                19,
                "Iron Muscle",
                "App/images/BusinessesLogos/fitness_equipments.jpg",
                """"All the sports equipment that you will need are here
                in the store for your convenient""",
                Website_Business.BusinessStatus.APPROVED,
                7,
                "store",
            ),
            (
                22,
                "My Protein",
                "App/images/BusinessesLogos/fitness_myprotein.jpg",
                """"Clothing, dietary needs, suppelments and more!""",
                Website_Business.BusinessStatus.APPROVED,
                7,
                "store",
            ),
            (
                22,
                "Crafting Materials",
                "App/images/BusinessesLogos/crafting_arta.jpg",
                """"Here you can buy a variety of products that match
                exactly your needs""",
                Website_Business.BusinessStatus.APPROVED,
                8,
                "store",
            ),
            (
                22,
                "Chocolate botique",
                "App/images/BusinessesLogos/chocolate.jpg",
                """"Hand made chocolate straight from coacoa beans to delicious
                botique chocolate with a secret recipe that make each bite full
                with rich flavor of chocolate.""",
                Website_Business.BusinessStatus.APPROVED,
                9,
                "store",
            ),
            (
                18,
                "Little Dairy Queen",
                "App/images/BusinessesLogos/food_dairy.jpg",
                """"Dairy products that belong to family up north with a big farm,
                 they raise the cows in the open air with no antibiotics
                 and its one of the healthiest milk in the country.""",
                Website_Business.BusinessStatus.APPROVED,
                9,
                "store",
            ),
            (
                10,
                "The old fisherman",
                "App/images/BusinessesLogos/food_fisherman.jpg",
                """"60 years of fishing family business.""",
                Website_Business.BusinessStatus.APPROVED,
                5,
                "store",
            ),
            (
                20,
                "Knife master",
                "App/images/BusinessesLogos/food_knife.jpg",
                """"The only place for our knife need. here you can find all
                kinds of knifes and accessories for them.""",
                Website_Business.BusinessStatus.APPROVED,
                5,
                "store",
            ),
            (
                20,
                "House of grill's",
                "App/images/BusinessesLogos/food_grills.jpg",
                """"We got grills!!!
                Come to us and get your grill today.""",
                Website_Business.BusinessStatus.APPROVED,
                5,
                "store",
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
                category,
            ) in business_test_data:
                website = Website.objects.filter(pk=website_id)[0]
                business = Business(
                    profile=get_object_or_404(Profile, pk=profile_id),
                    name=name,
                    logo=logo,
                    description=description,
                )
                business.save()
                website.match_business_to_website(business, is_confirmed, category)

    operations = [
        migrations.RunPython(generate_data),
    ]
