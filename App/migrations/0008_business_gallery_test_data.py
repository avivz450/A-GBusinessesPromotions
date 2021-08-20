from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0007_categories_test_data"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Business_Image, Business
        from django.shortcuts import get_object_or_404

        business_image_test_data = [
            (
                1,
                "App/images/BusinessesGallery/demo_business_1_1.png",
            ),
            (
                1,
                "App/images/BusinessesGallery/demo_business_1_2.png",
            ),
            (
                1,
                "App/images/BusinessesGallery/demo_business_1_3.png",
            ),
            (
                1,
                "App/images/BusinessesGallery/demo_business_1_4.png",
            ),
            (
                1,
                "App/images/BusinessesGallery/demo_business_1_5.png",
            ),
            (
                2,
                "App/images/BusinessesGallery/demo_business_2_1.png",
            ),
            (
                2,
                "App/images/BusinessesGallery/demo_business_2_2.png",
            ),
            (
                2,
                "App/images/BusinessesGallery/demo_business_2_3.png",
            ),
            (
                2,
                "App/images/BusinessesGallery/demo_business_2_4.png",
            ),
            (
                2,
                "App/images/BusinessesGallery/demo_business_2_5.png",
            ),
            (
                3,
                "App/images/BusinessesGallery/demo_business_3_1.png",
            ),
            (
                3,
                "App/images/BusinessesGallery/demo_business_3_2.png",
            ),
            (
                3,
                "App/images/BusinessesGallery/demo_business_3_3.png",
            ),
            (
                3,
                "App/images/BusinessesGallery/demo_business_3_4.png",
            ),
            (
                3,
                "App/images/BusinessesGallery/demo_business_3_5.png",
            ),
            (
                4,
                "App/images/BusinessesGallery/vegan_business_1_1.jpg",
            ),
            (
                4,
                "App/images/BusinessesGallery/vegan_business_1_2.jpg",
            ),
            (
                4,
                "App/images/BusinessesGallery/vegan_business_1_3.jfif",
            ),
            (
                4,
                "App/images/BusinessesGallery/vegan_business_1_4.jpg",
            ),
            (
                4,
                "App/images/BusinessesGallery/vegan_business_1_5.jpg",
            ),
            (
                5,
                "App/images/BusinessesGallery/vegan_business_2_1.jfif",
            ),
            (
                5,
                "App/images/BusinessesGallery/vegan_business_2_2.png",
            ),
            (
                5,
                "App/images/BusinessesGallery/vegan_business_2_3.jpg",
            ),
            (
                5,
                "App/images/BusinessesGallery/vegan_business_2_4.jpg",
            ),
            (
                5,
                "App/images/BusinessesGallery/vegan_business_2_5.jpg",
            ),
            (
                6,
                "App/images/BusinessesGallery/vegan_business_3_1.jfif",
            ),
            (
                6,
                "App/images/BusinessesGallery/vegan_business_3_2.png",
            ),
            (
                6,
                "App/images/BusinessesGallery/vegan_business_3_3.jpeg",
            ),
            (
                6,
                "App/images/BusinessesGallery/vegan_business_3_4.jpg",
            ),
            (
                6,
                "App/images/BusinessesGallery/vegan_business_3_5.jfif",
            ),
            (
                7,
                "App/images/BusinessesGallery/coffe_botique_1.jpg",
            ),
            (
                7,
                "App/images/BusinessesGallery/coffe_botique_2.jfif",
            ),
            (
                7,
                "App/images/BusinessesGallery/coffe_botique_3.jfif",
            ),
            (
                7,
                "App/images/BusinessesGallery/coffe_botique_4.jpg",
            ),
            (
                7,
                "App/images/BusinessesGallery/coffe_botique_5.jfif",
            ),
            (
                8,
                "App/images/BusinessesGallery/ninja_1.jpg",
            ),
            (
                8,
                "App/images/BusinessesGallery/ninja_2.jpg",
            ),
            (
                8,
                "App/images/BusinessesGallery/ninja_3.jpg",
            ),
            (
                8,
                "App/images/BusinessesGallery/ninja_4.jfif",
            ),
            (
                8,
                "App/images/BusinessesGallery/ninja_5.jfif",
            ),
            (
                9,
                "App/images/BusinessesGallery/butcher_1.jpg",
            ),
            (
                9,
                "App/images/BusinessesGallery/butcher_2.jpeg",
            ),
            (
                9,
                "App/images/BusinessesGallery/butcher_3.jpg",
            ),
            (
                9,
                "App/images/BusinessesGallery/butcher_4.jfif",
            ),
            (
                9,
                "App/images/BusinessesGallery/butcher_5.jpg",
            ),
            (
                10,
                "App/images/BusinessesGallery/candy_shop_1.jfif",
            ),
            (
                10,
                "App/images/BusinessesGallery/candy_shop_2.jfif",
            ),
            (
                10,
                "App/images/BusinessesGallery/candy_shop_3.jpg",
            ),
            (
                10,
                "App/images/BusinessesGallery/candy_shop_4.jpg",
            ),
            (
                10,
                "App/images/BusinessesGallery/candy_shop_5.png",
            ),
            (
                11,
                "App/images/BusinessesGallery/weights_shop_1.jpg",
            ),
            (
                11,
                "App/images/BusinessesGallery/weights_shop_2.jfif",
            ),
            (
                11,
                "App/images/BusinessesGallery/weights_shop_3.jfif",
            ),
            (
                11,
                "App/images/BusinessesGallery/weights_shop_4.jpg",
            ),
            (
                11,
                "App/images/BusinessesGallery/weights_shop_5.jpg",
            ),
            (
                12,
                "App/images/BusinessesGallery/my_protein_1.jfif",
            ),
            (
                12,
                "App/images/BusinessesGallery/my_protein_2.jfif",
            ),
            (
                12,
                "App/images/BusinessesGallery/my_protein_3.jfif",
            ),
            (
                12,
                "App/images/BusinessesGallery/my_protein_4.png",
            ),
            (
                12,
                "App/images/BusinessesGallery/my_protein_5.jpg",
            ),
            (
                13,
                "App/images/BusinessesGallery/crafting_shop_1.jfif",
            ),
            (
                13,
                "App/images/BusinessesGallery/crafting_shop_2.jpg",
            ),
            (
                13,
                "App/images/BusinessesGallery/crafting_shop_3.jfif",
            ),
            (
                13,
                "App/images/BusinessesGallery/crafting_shop_4.jfif",
            ),
            (
                13,
                "App/images/BusinessesGallery/crafting_shop_5.jfif",
            ),
            (
                14,
                "App/images/BusinessesGallery/chocolate_botique_1.jpg",
            ),
            (
                14,
                "App/images/BusinessesGallery/chocolate_botique_2.jfif",
            ),
            (
                14,
                "App/images/BusinessesGallery/chocolate_botique_3.jpg",
            ),
            (
                14,
                "App/images/BusinessesGallery/chocolate_botique_4.jpg",
            ),
            (
                14,
                "App/images/BusinessesGallery/chocolate_botique_5.jpg",
            ),
            (
                15,
                "App/images/BusinessesGallery/dairy_queen_1.jfif",
            ),
            (
                15,
                "App/images/BusinessesGallery/dairy_queen_2.jpg",
            ),
            (
                15,
                "App/images/BusinessesGallery/dairy_queen_3.jpg",
            ),
            (
                15,
                "App/images/BusinessesGallery/dairy_queen_4.jpg",
            ),
            (
                15,
                "App/images/BusinessesGallery/dairy_queen_5.jpg",
            ),
            (
                16,
                "App/images/BusinessesGallery/the_old_fisherman_1.jpg",
            ),
            (
                16,
                "App/images/BusinessesGallery/the_old_fisherman_2.jfif",
            ),
            (
                16,
                "App/images/BusinessesGallery/the_old_fisherman_3.jpg",
            ),
            (
                16,
                "App/images/BusinessesGallery/the_old_fisherman_4.jfif",
            ),
            (
                16,
                "App/images/BusinessesGallery/the_old_fisherman_5.jpg",
            ),
            (
                17,
                "App/images/BusinessesGallery/knife_master_1.jfif",
            ),
            (
                17,
                "App/images/BusinessesGallery/knife_master_2.jfif",
            ),
            (
                17,
                "App/images/BusinessesGallery/knife_master_3.jfif",
            ),
            (
                17,
                "App/images/BusinessesGallery/knife_master_4.jfif",
            ),
            (
                17,
                "App/images/BusinessesGallery/knife_master_5.jpg",
            ),
            (
                18,
                "App/images/BusinessesGallery/grill_store_1.jfif",
            ),
            (
                18,
                "App/images/BusinessesGallery/grill_store_2.jfif",
            ),
            (
                18,
                "App/images/BusinessesGallery/grill_store_3.jfif",
            ),
            (
                18,
                "App/images/BusinessesGallery/grill_store_4.jfif",
            ),
            (
                18,
                "App/images/BusinessesGallery/grill_store_5.jfif",
            ),
        ]

        with transaction.atomic():
            for business_id, image in business_image_test_data:
                business_image = Business_Image(
                    business=get_object_or_404(Business, pk=business_id),
                    image=image,
                )
                business_image.save()

    operations = [
        migrations.RunPython(generate_data),
    ]