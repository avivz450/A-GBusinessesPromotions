from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0014_alter_website_logo"),
    ]

    def generate_data(apps, schema_editor):
        from App.models import Website, Profile
        from django.shortcuts import get_object_or_404

        website_test_data = [
            ("Demo"),
        ]

        with transaction.atomic():
            for website_name in website_test_data:
                website = Website(name=website_name)
                website.save()
                profile = get_object_or_404(Profile, pk=4)
                profile.match_website_to_profile(website)

    operations = [
        migrations.RunPython(generate_data),
    ]
