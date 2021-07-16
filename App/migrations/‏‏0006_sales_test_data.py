from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "‏‏0005_businesses_test_data"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Sale, Profile, Business
        from django.shortcuts import get_object_or_404

        sales_test_data = [
            (
                4,
                1,
                "Sale demo 1",
                "description description description description description description",
                "App/images/SalesPictures/demo_sale_1.png",
                True,
            ),
            (
                4,
                3,
                "Sale demo 2",
                "description description description description description description",
                "App/images/SalesPictures/demo_sale_2.png",
                True,
            ),
            (
                4,
                6,
                "30% discount on rosemary oil",
                "And other various diescounts on our oils!",
                "App/images/SalesPictures/vegan_sale_2.png",
                True,
            ),
            (
                4,
                4,
                "Special offers on orders on Friday!",
                "Reservations can be made until Wednesday at 16:00",
                "App/images/SalesPictures/vegan_sale_1.jpg",
                True,
            ),
        ]

        with transaction.atomic():
            for (
                profile_id,
                business_id,
                title,
                description,
                picture,
                is_confirmed,
            ) in sales_test_data:
                sale = Sale(
                    profile=get_object_or_404(Profile, pk=profile_id),
                    business=get_object_or_404(Business, pk=business_id),
                    title=title,
                    picture=picture,
                    description=description,
                    is_confirmed=is_confirmed,
                )
                sale.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
