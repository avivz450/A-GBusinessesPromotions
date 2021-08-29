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
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/demo_business_1.png",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
                1,
                "demo",
            ),
            (
                21,
                "Business demo 2",
                "App/images/BusinessesLogos/demo_business_2_logo.png",
                "Business demo 2 description",
                "",
                "",
                "",
                Website_Business.BusinessStatus.PENDING,
                "App/images/BusinessesMainPictures/demo_business_2.png",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
                1,
                "demo",
            ),
            (
                21,
                "Business demo 3",
                "App/images/BusinessesLogos/demo_business_3_logo.png",
                "Business demo 3 description",
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/demo_business_3.png",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
                1,
                "demo",
            ),
            (
                21,
                "MikiMaya",
                "App/images/BusinessesLogos/vegan_business_1_logo.jpg",
                "Mikimaya is a vegan restaurant in the town of Tzur Moshe, where you will find a menu rich in flavors.",
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/vegan_business_1.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
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
                "",
                "",
                "",
                Website_Business.BusinessStatus.PENDING,
                "App/images/BusinessesMainPictures/vegan_business_2.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
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
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/vegan_business_3.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
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
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/caffe_botique.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Sarona Market, Tel Aviv-Yafo",
                ("32.07114205438995, 34.7872861930747"),
                3,
                "food",
            ),
            (
                22,
                "Ninja",
                "App/images/BusinessesLogos/food_ninja.jpg",
                """"Electric kitchen machines.""",
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/ninja.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
                4,
                "store",
            ),
            (
                22,
                "The Big Butcher",
                "App/images/BusinessesLogos/food_butcher.jpg",
                """"Botique butcher with the most delicious meats.""",
                "facebook/the_big_butcher",
                "instagram/the_big_butcher/",
                "youtube.com/c/TheBigButcher",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/buthcer.jfif",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Marzouk and Azar 10, Tel Aviv-Yafo",
                ("32.055059, 34.759112"),
                5,
                "food",
            ),
            (
                22,
                "Lets Go To The Candy Shop",
                "App/images/BusinessesLogos/food_candies.jpg",
                """"Candies candies and more candies, all kinds of candies in variety
                of flavors and colors.""",
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/candies.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Menachem Begin, Tel Aviv-Yafo",
                ("32.074154, 34.790952"),
                6,
                "food",
            ),
            (
                19,
                "Iron Muscle",
                "App/images/BusinessesLogos/fitness_equipments.jpg",
                """"All the sports equipment that you will need are here
                in the store for your convenient""",
                "facebook/iron_muscle",
                "instagram/iron_muscle/",
                "youtube.com/c/IronMuscle",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/weights.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "HaYarkon 165, Tel Aviv-Yafo",
                ("32.084628, 34.769798"),
                7,
                "store",
            ),
            (
                22,
                "My Protein",
                "App/images/BusinessesLogos/fitness_myprotein.png",
                """"Clothing, dietary needs, suppelments and more!""",
                "facebook/my_protein",
                "instagram/my_protein/",
                "youtube.com/c/MyProtein",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/protein.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "King George St 47, Tel Aviv-Yafo",
                ("32.073491, 34.775162"),
                7,
                "store",
            ),
            (
                22,
                "Crafting Materials",
                "App/images/BusinessesLogos/crafting_arta.jpg",
                """"Here you can buy a variety of products that match
                exactly your needs""",
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/crafting.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Nahalat Binyamin 83, Tel Aviv-Yafo",
                ("32.0612662,34.7725918"),
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
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/chocolate.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Sarona Market, Tel Aviv-Yafo",
                ("32.07114205438995, 34.7872861930747"),
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
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/dairy.jfif",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Shlomo Ibn Gabirol 96, Tel Aviv-Yafo",
                ("32.084188, 34.781623"),
                9,
                "store",
            ),
            (
                10,
                "The old fisherman",
                "App/images/BusinessesLogos/food_fisherman.jpg",
                """"60 years of fishing family business.""",
                "facebook/the_old_fisherman",
                "instagram/the_old_fisherman/",
                "youtube.com/c/TheOldFisherman",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/fish.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Sderot Yerushalayim 9, Tel Aviv-Yafo",
                ("32.056046, 34.759809"),
                5,
                "store",
            ),
            (
                20,
                "Knife master",
                "App/images/BusinessesLogos/food_knife.jpg",
                """"The only place for our knife need. here you can find all
                kinds of knifes and accessories for them.""",
                "facebook/knife_master",
                "instagram/knife_master/",
                "youtube.com/c/KnifeMaster",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/dairy.jfif",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Sarona Market, Tel Aviv-Yafo",
                ("32.07114205438995, 34.7872861930747"),
                5,
                "store",
            ),
            (
                20,
                "House of grill's",
                "App/images/BusinessesLogos/food_grills.jpg",
                """"We got grills!!!
                Come to us and get your grill today.""",
                "facebook/house_of_grill",
                "instagram/house_of_grill/",
                "youtube.com/c/HouseOfGrill",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/grill.jfif",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Allenby 110, Tel Aviv-Yafo",
                ("32.064600,34.772665"),
                5,
                "store",
            ),
            (
                20,
                "Shoe Store",
                "App/images/BusinessesLogos/shoe_store.jpg",
                """"We got all the shoe's variety, for running, crossfit,
                lifting and more""",
                "facebook/shoe_store",
                "instagram/shoe_store/",
                "youtube.com/c/ShoeStore",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/shoe_store.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Zamenhof 2, Tel Aviv-Yafo",
                ("32.077849,34.775154"),
                7,
                "store",
            ),
            (
                20,
                "Sports Wear",
                "App/images/BusinessesLogos/sports_wear.jfif",
                """"Here you can find shorts, leggings, shirts, skirts
                and more""",
                "facebook/sports_wear",
                "instagram/sports_wear/",
                "youtube.com/c/SportsWear",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/sports_wear.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Yehoshua Hatalmi 16, Tel Aviv-Yafo",
                ("32.062617,34.768776"),
                7,
                "store",
            ),
            (
                16,
                "Sports Equipment",
                "App/images/BusinessesLogos/sports_equipment.jfif",
                """"Basketball, soccer, tennis and more...""",
                "facebook/sports_equipment",
                "instagram/sports_equipment/",
                "youtube.com/c/SportsEquipment",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/sports_equipment.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Allenby St 113, Tel Aviv-Yafo",
                ("32.062704,34.773283"),
                7,
                "store",
            ),
            (
                15,
                "Climbing Store",
                "App/images/BusinessesLogos/climbing_store.png",
                """"We are the biggest climbing supply store
                in the all city""",
                "facebook/climbing_store",
                "instagram/climbing_store/",
                "youtube.com/c/ClimbingStore",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/climbing_store.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Derech Qibbutz 26, Tel Aviv-Yafo",
                ("32.051941, 34.767453"),
                7,
                "store",
            ),
            (
                14,
                "Diving Store",
                "App/images/BusinessesLogos/diving_store.jfif",
                """"All the diving equipment that you
                would ever need is here in our store""",
                "facebook/diving_store",
                "instagram/diving_store/",
                "youtube.com/c/DivingStore",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/diving_store.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "HaPatish 10, Tel Aviv-Yafo",
                ("32.051463,34.771668"),
                7,
                "store",
            ),
            (
                16,
                "Bones",
                "App/images/BusinessesLogos/bones_restaurant.png",
                """"Meat specialized restaurant
                """,
                "facebook/bones",
                "instagram/bones/",
                "youtube.com/c/Bones",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/bones_restaurant.jpg",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Shlomo Ibn Gabirol St 118, Tel Aviv-Yafo",
                ("32.085892,34.781973"),
                5,
                "restaurant",
            ),
            (
                15,
                "Coffee Machines",
                "App/images/BusinessesLogos/coffee_machine.png",
                """"We have all the coffee machines
                you will ever need""",
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/coffee_machine.jfif",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Pinsker St 72, Tel Aviv-Yafo",
                ("32.077622,34.773852"),
                3,
                "store",
            ),
            (
                14,
                "Coffee House",
                "App/images/BusinessesLogos/coffee_house.jfif",
                """"Coffee house since 1814
                """,
                "",
                "",
                "",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/coffee_house.jfif",
                "09:00:00",
                "18:00:00",
                "+972501234567",
                5,
                "Dizengoff Square 4, Tel Aviv-Yafo",
                ("32.077792,34.774548"),
                3,
                "restaurant",
            ),
        ]

        with transaction.atomic():
            for (
                profile_id,
                name,
                logo,
                description,
                facebook_link,
                instagram_link,
                youtube_link,
                is_confirmed,
                main_picture,
                from_hour,
                to_hour,
                phone_number,
                number_of_additional_pictures,
                location,
                location_points,
                website_id,
                category,
            ) in business_test_data:
                website = Website.objects.filter(pk=website_id)[0]
                business = Business(
                    profile=get_object_or_404(Profile, pk=profile_id),
                    name=name,
                    logo=logo,
                    description=description,
                    facebook_link=facebook_link,
                    instagram_link=instagram_link,
                    youtube_link=youtube_link,
                    main_picture=main_picture,
                    from_hour=from_hour,
                    to_hour=to_hour,
                    phone_number=phone_number,
                    number_of_additional_pictures=number_of_additional_pictures,
                    location=location,
                    location_points=location_points,
                )
                business.save()
                website.match_business_to_website(business, is_confirmed, category)

    operations = [
        migrations.RunPython(generate_data),
    ]
