from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0003_website_test_data"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Slide, Website
        from django.shortcuts import get_object_or_404

        slide_test_data = [
            (
                1,
                "Tel Aviv City",
                """Located in the center of Israel, populated in diversity of people, work places,
                memorials, hangout places, you can choose apartments in a tall building to a
                private house.
""",
                "App/images/SlidePictures/test_data/Tel_Aviv/slide1.jpg",
            ),
            (
                1,
                "",
                """One of the most populated area in israel that also near to the beach,
                attracts a lot of tourists every year and a symbol to tolerance.
""",
                "App/images/SlidePictures/test_data/Tel_Aviv/slide2.jpg",
            ),
            (
                2,
                "Welcome to Vegan lovers!",
                """Vegan refers to anything that’s free of animal products: No meat, fish, milk,
                cheese, eggs, wool, leather, honey and so forth.
                Digging deeper into the word’s meaning will make you a more effective and persuasive advocate of
                 all vegan-oriented concerns.
""",
                "App/images/SlidePictures/test_data/Vegan/slide1.jpg",
            ),
            (
                2,
                "Why Go Vegan?",
                """A vegan lifestyle can support incredible health and protect huge numbers of animals,
                 while simultaneously combating climate change.
                 Plus, the food is insanely delicious and becomes more widely available every year.
""",
                "App/images/SlidePictures/test_data/Vegan/slide2.jpg",
            ),
            (
                2,
                "What do vegans eat?",
                """Absolutely loads of stuff.
                There’s a misconception that vegans only eat ‘vegetables’,
                 but the better way to think of it is that vegans eat plants.
                Once you do that, you realise that this means potatoes,
                rice, pasta, bread, lentils, chickpeas, beans, soy,
                 grains, seeds, nuts, fruits, oils, and vegetables, among others.
""",
                "App/images/SlidePictures/test_data/Vegan/slide3.jpg",
            ),
            (
                3,
                "Welcome To Coffee Lovers!",
                """In this website yo will find every desire that make your senses to dance..
""",
                "App/images/SlidePictures/test_data/Coffee/slide1.jpg",
            ),
            (
                3,
                "Coffee Product",
                """Here you can find different topics that every coffee lover will be glad to have
                from fresh beans to advanced coffee makers.
""",
                "App/images/SlidePictures/test_data/Coffee/slide2.jpg",
            ),
            (
                4,
                "The Best Electronics",
                """We have the best product gurenteed, full life time care on all the store.
""",
                "App/images/SlidePictures/test_data/Electronics/slide1.jpg",
            ),
            (
                4,
                "House Gadgets",
                """You will be able to find electrincs for the kitchen, toilet, bedroom, tv room,
                and more to make your home more advanced
""",
                "App/images/SlidePictures/test_data/Electronics/slide2.jpg",
            ),
            (
                5,
                "Place Of Meats",
                """We have free range animals meat with no antibiotics and supplements, well care meats straight
                from the farmer to your table.
""",
                "App/images/SlidePictures/test_data/Carnibors/slide1.jpg",
            ),
            (
                5,
                "For Every One",
                """If you are new, intermidate or advanced, we are sure u can find the right business
                for you.
""",
                "App/images/SlidePictures/test_data/Carnibors/slide2.jpg",
            ),
            (
                6,
                "Candies",
                """Its sweet, its sour, its salty and its yummy!!!
""",
                "App/images/SlidePictures/test_data/Candies/slide1.jpg",
            ),
            (
                6,
                "Did you taste them all?",
                """Here you can find a big amount of different candies to your taste.
""",
                "App/images/SlidePictures/test_data/Candies/slide2.jpg",
            ),
            (
                7,
                "Welcome To Fitness Lifestyle!",
                """The complete fitness community online.
""",
                "App/images/SlidePictures/test_data/Fitness/slide1.jpg",
            ),
            (
                7,
                "fitness is for every one",
                """Today we know how much important is to exrecize to maintaining
                an healthy life, body and mind.
""",
                "App/images/SlidePictures/test_data/Fitness/slide2.jpg",
            ),
            (
                7,
                "Products And More",
                """Here you can find what ever fitness product you will need
                from home gym, outdoors sports and different supplements.
""",
                "App/images/SlidePictures/test_data/Fitness/slide3.jpg",
            ),
            (
                8,
                "Welcome To Crafting World!",
                """Here you can find all kinds of different craftings areas.
""",
                "App/images/SlidePictures/test_data/Crafting/slide1.jpg",
            ),
            (
                8,
                "Are You Enthusiastic About Crafting",
                """Some times its can be hard to find crafting products
                and materials, so here you can find all kinds of different
                stores to get what you need.
""",
                "App/images/SlidePictures/test_data/Crafting/slide2.jpg",
            ),
            (
                9,
                "Dairy",
                """Makes your body strong, raise bones density, giving you good vitamins
                and healthy for your diet.
""",
                "App/images/SlidePictures/test_data/Dairy/slide1.jpg",
            ),
            (
                9,
                "Products",
                """Its not surprise that dairy is in most of our food that we cunsume each cay,
                so here you will be able to find all the good tnigs that made from milk.
""",
                "App/images/SlidePictures/test_data/Dairy/slide2.jpg",
            ),
        ]

        with transaction.atomic():
            for website_id, title, description, photo in slide_test_data:
                slide = Slide(
                    website=get_object_or_404(Website, pk=website_id),
                    title=title,
                    description=description,
                    picture=photo,
                )
                slide.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
