# Generated by Django 3.2.5 on 2021-07-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0004_auto_20210711_0950"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slide",
            name="description",
            field=models.TextField(default=None, max_length=200),
        ),
    ]
