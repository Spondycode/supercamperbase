# Generated by Django 4.2.7 on 2023-11-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_plot", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plot",
            name="what3words",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
