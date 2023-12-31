# Generated by Django 4.2.7 on 2023-12-27 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("a_plot", "0018_alter_comment_options_reply"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikedPlot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "plot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="a_plot.plot"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="plot",
            name="likes",
            field=models.ManyToManyField(
                related_name="likedplots",
                through="a_plot.LikedPlot",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
