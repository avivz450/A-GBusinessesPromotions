# Generated by Django 3.2.5 on 2021-10-05 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0008_business_gallery_test_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="hours",
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
