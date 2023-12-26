# Generated by Django 4.2.7 on 2023-12-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_user", "0003_alter_profile_campermode"),
    ]

    operations = [
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
                    ("Caravan", "Caravan"),
                    ("Under the Stars", "Under the Stars"),
                ],
                default="Hammock",
                max_length=20,
                null=True,
            ),
        ),
    ]