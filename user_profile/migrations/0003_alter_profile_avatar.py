# Generated by Django 4.1 on 2022-08-21 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="media/profiles/nofile.png", upload_to="media/profiles"
            ),
        ),
    ]