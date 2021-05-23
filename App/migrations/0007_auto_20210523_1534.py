# Generated by Django 3.2.3 on 2021-05-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_business_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='URL',
            field=models.URLField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='business',
            name='facebook_link',
            field=models.URLField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='business',
            name='instagram_link',
            field=models.URLField(default=None, max_length=250),
        ),
    ]