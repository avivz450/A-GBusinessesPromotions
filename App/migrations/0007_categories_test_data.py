from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "‏‏0006_sales_test_data"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Website, Business_Category

        categories_test_data = [
            (
                1,
                "demo",
            ),
            (
                2,
                "vegan",
            ),
            (
                2,
                "food",
            ),
            (
                2,
                "drinks",
            ),
            (
                2,
                "store",
            ),
            (
                3,
                "food",
            ),
            (
                3,
                "drinks",
            ),
            (
                3,
                "store",
            ),
            (
                4,
                "store",
            ),
            (
                5,
                "food",
            ),
            (
                5,
                "store",
            ),
            (
                6,
                "store",
            ),
            (
                6,
                "food",
            ),
            (
                7,
                "store",
            ),
            (
                7,
                "food",
            ),
            (
                8,
                "store",
            ),
            (
                9,
                "store",
            ),
            (
                9,
                "food",
            ),
            (
                9,
                "drinks",
            ),
        ]

        with transaction.atomic():
            for (
                website_id,
                category_name,
            ) in categories_test_data:
                business_Category = Business_Category(
                    website=Website.objects.filter(pk=website_id)[0],
                    category_name=category_name,
                )
                business_Category.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
