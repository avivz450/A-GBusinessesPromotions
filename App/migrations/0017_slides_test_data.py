from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0016_website_test_data"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Slide, Website
        from django.shortcuts import get_object_or_404

        slide_test_data = [
            (
                1,
                "Welcome to a website demo!",
                "This site is designed to give you a glimpse of what your site will look like once you create it. ",
                "App/images/SlidePictures/test_data/Website_Demo/slide1.jpg",
            ),
            (
                1,
                "How it works?",
                """Our goal is to advertise the businesses whose types are related to your site. 
All you need to do is create a website on our platform, and copy that URL to your original site.
As an admin, you choose which businesses and sales will be shown on your site which is on our platform.
""",
                "App/images/SlidePictures/test_data/Website_Demo/slide2.png",
            ),
            (
                2,
                "Welcome to Vegan lovers!",
                """Vegan refers to anything that’s free of animal products: No meat, fish, milk, cheese, eggs, wool, leather, honey and so forth.
                Digging deeper into the word’s meaning will make you a more effective and persuasive advocate of all vegan-oriented concerns.
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
                There’s a misconception that vegans only eat ‘vegetables’, but the better way to think of it is that vegans eat plants. 
                Once you do that, you realise that this means potatoes, 
                rice, pasta, bread, lentils, chickpeas, beans, soy, grains, seeds, nuts, fruits, oils, and vegetables, among others.
""",
                "App/images/SlidePictures/test_data/Vegan/slide3.jpg",
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
