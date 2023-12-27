# Generated by Django 4.2.7 on 2023-12-27 20:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("a_plot", "0020_rename_post_likedpost_plot"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="LikedPost",
            new_name="LikedPlot",
        ),
        migrations.AlterField(
            model_name="plot",
            name="likes",
            field=models.ManyToManyField(
                related_name="likedplots",
                through="a_plot.LikedPost",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
