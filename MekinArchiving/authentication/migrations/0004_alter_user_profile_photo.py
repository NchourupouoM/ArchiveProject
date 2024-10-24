# Generated by Django 5.1.1 on 2024-10-21 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_alter_user_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                default="/media/profil.png",
                upload_to="",
                verbose_name="Photo de profil",
            ),
        ),
    ]
