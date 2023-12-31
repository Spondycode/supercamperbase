# Generated by Django 4.2.7 on 2023-12-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_plot", "0011_plot_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plot",
            name="categories",
            field=models.IntegerField(
                choices=[
                    ("Campsite", "Campsite"),
                    ("Official", "Official"),
                    ("Wild", "Wild"),
                ],
                default=1,
            ),
        ),
    ]
