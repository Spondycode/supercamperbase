# Generated by Django 4.2.7 on 2024-01-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_user", "0008_profile_fav_campsite_alter_profile_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="numplots",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SC_Founder1", "SuperCamper Founder1"),
                    ("SC_Founder2", "SuperCamper Founder2"),
                    ("New_SuperCamper", "New SuperCamper"),
                    ("SuperCamper", "SuperCamper"),
                    ("SuperCamper Expert", "SuperCamper Expert"),
                    ("SuperCamper Master", "SuperCamper Master"),
                    ("Restricted SuperCamper", "Restricted SuperCamper"),
                    ("Banned", "Banned"),
                ],
                default="New SuperCamper",
                max_length=30,
                null=True,
            ),
        ),
    ]
