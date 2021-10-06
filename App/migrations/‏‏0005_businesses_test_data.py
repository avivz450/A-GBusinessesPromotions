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
                22,
                "MattDoesFitness",
                "App/images/BusinessesLogos/matt_does_fitness.jfif",
                """"Personal trainings one on one and a groups sessions""",
                "https://facebook.com/matt_does_fitness",
                "https://instagram.com/matt_does_fitness/",
                "https://youtube.com/user/MattDoesFitness",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/matt_does_fitness.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
                "+972501234567",
                5,
                "Shlomo Ibn Gabirol 96, Tel Aviv-Yafo",
                ("32.084188, 34.781623"),
                7,
                "trainer",
            ),
            (
                22,
                "Space Florentin",
                "App/images/BusinessesLogos/space_florentin.jfif",
                """"Space GYM""",
                "https://facebook.com/space_florentin",
                "https://instagram.com/space_florentin/",
                "https://youtube.com/user/SpaceFlorentin",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/space_florentin.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
                "+972501234567",
                5,
                "Shalma Rd 45, Tel Aviv-Yafo",
                ("32.055040, 34.766299"),
                7,
                "gym",
            ),
            (
                22,
                "Lake TLV",
                "App/images/BusinessesLogos/lake_tlv.png",
                """"Water Sports""",
                "https://facebook.com/lake_tlv",
                "https://instagram.com/lake_tlv/",
                "https://youtube.com/user/LakeTLV",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/lake_tlv.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
                "+972501234567",
                5,
                "פארק דרום פארק מנחם בגין, Tel Aviv-Yafo",
                ("32.041297, 34.803268"),
                7,
                "sports",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "App/images/BusinessesLogos/vegan_business_2_logo.png",
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
                "App/images/BusinessesMainPictures/vegan_business_2.png",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """
                    Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/the_big_butcher",
                "https://instagram.com/the_big_butcher/",
                "https://youtube.com/c/TheBigButcher",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/buthcer.jfif",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/iron_muscle",
                "https://instagram.com/iron_muscle/",
                "https://youtube.com/c/IronMuscle",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/weights.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/my_protein",
                "https://instagram.com/my_protein/",
                "https://youtube.com/c/MyProtein",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/protein.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/the_old_fisherman",
                "https://instagram.com/the_old_fisherman/",
                "https://youtube.com/c/TheOldFisherman",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/fish.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/knife_master",
                "https://instagram.com/knife_master/",
                "https://youtube.com/c/KnifeMaster",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/dairy.jfif",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/house_of_grill",
                "https://instagram.com/house_of_grill/",
                "https://youtube.com/c/HouseOfGrill",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/grill.jfif",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/shoe_store",
                "https://instagram.com/shoe_store/",
                "https://youtube.com/c/ShoeStore",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/shoe_store.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/sports_wear",
                "https://instagram.com/sports_wear/",
                "https://youtube.com/c/SportsWear",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/sports_wear.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/sports_equipment",
                "https://instagram.com/sports_equipment/",
                "https://youtube.com/c/SportsEquipment",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/sports_equipment.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/climbing_store",
                "https://instagram.com/climbing_store/",
                "https://youtube.com/c/ClimbingStore",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/climbing_store.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/diving_store",
                "https://instagram.com/diving_store/",
                "https://youtube.com/c/DivingStore",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/diving_store.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                "https://facebook.com/bones",
                "https://instagram.com/bones/",
                "https://youtube.com/c/Bones",
                Website_Business.BusinessStatus.APPROVED,
                "App/images/BusinessesMainPictures/bones_restaurant.jpg",
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                """ Sun: 9 a.m. - 6 p.m.
                    Mon: 9 a.m. - 6 p.m.
                    Tue: 9 a.m. - 6 p.m.
                    Wed: 9 a.m. - 6 p.m.
                    Thu: 9 a.m. - 6 p.m.
                    Fri: 9 a.m. - 3 p.m.
                    Sat: close
""",
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
                hours,
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
                    hours=hours,
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
