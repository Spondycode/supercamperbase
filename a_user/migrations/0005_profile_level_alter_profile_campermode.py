# Generated by Django 4.2.7 on 2024-01-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_user", "0004_alter_profile_campermode"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("New SuperCamper", "New SuperCamper"),
                    ("SuperCamper", "SuperCamper"),
                    ("SuperCamper Expert", "SuperCamper Expert"),
                    ("SuperCamper Master", "SuperCamper Master"),
                ],
                default="New SuperCamper",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="campermode",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Hammock", "Hammock"),
                    ("Small Tent", "Small Tent"),
                    ("Large Tent", "Large tent"),
                    ("Car", "Car"),
                    ("Van", "Van"),
                    ("CamperVan", "CamperVan"),
                    ("Motorhome", "Motorhome"),
                    ("Small Caravan", "Small Caravan"),
                    ("Large Caravan", "Large Caravan"),
                    ("Trailer Tent", "Trailer Tent"),
                    ("Under the Stars", "Under the Stars"),
                ],
                default="Hammock",
                max_length=20,
                null=True,
            ),
        ),
    ]
