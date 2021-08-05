from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0001_initial"),
    ]

    def generate_data(apps, schema_editor):
        from django.contrib.auth.models import User
        from App.models import Profile

        user_test_data = [
            ("Shachar", "ShacharShachar", "Shachar@gmail.com"),
            ("Liat", "LiatLiat", "Liat@gmail.com"),
            ("Bella", "BellaBella", "Bella@gmail.com"),
            ("Dana", "DanaDana", "Dana@gmail.com"),
            ("Josh", "JoshJosh", "Josh@gmail.com"),
            ("Drake", "DrakeDrake", "Drake@gmail.com"),
            ("Ash", "AshAsh", "Ash@gmail.com"),
            ("Goku", "GokuGoku", "Goku@gmail.com"),
            ("Jon", "JonJon", "Jon@gmail.com"),
            ("Misty", "MistyMisty", "Misty@gmail.com"),
            ("Zafrani", "ZafraniZafrani", "Zafrani@gmail.com"),
            ("Brock", "BrockBrock", "Brock@gmail.com"),
            ("Maor", "MaorMaor", "Maor@gmail.com"),
            ("Refael", "RefaelRefael", "Refael@gmail.com"),
            ("Logan", "LoganLogan", "Logan@gmail.com"),
            ("Peter", "PeterPeter", "Peter@gmail.com"),
            ("Parker", "ParkerParker", "Parker@gmail.com"),
            ("Tony", "TonyTony", "Tony@gmail.com"),
            ("Stark", "StarkStark", "Stark@gmail.com"),
            ("Groot", "GrootGroot", "Groot@gmail.com"),
        ]

        with transaction.atomic():
            # Test: Create a User and Profile from a User via username.
            for username, password, email in user_test_data:
                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                Profile(user=user).save()
            # Test: Create a Profile with user who was updated to superuser (admin)
            user1 = User.objects.create_superuser(
                username="Aviv", password="AvivAviv", email="Avivz450@gmail.com"
            ).save()
            user2 = User.objects.create_superuser(
                username="Gideon",
                password="GideonGideon",
                email="gideonshachar@gmail.com",
            ).save()
            Profile(user=user1, is_vip=True).save()
            Profile(user=user2, is_vip=True).save()
            # Test: Update a profile to be blocked.
            profile = Profile.objects.get(user=User.objects.get(username="Bella"))
            profile.is_blocked = True
            profile.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
