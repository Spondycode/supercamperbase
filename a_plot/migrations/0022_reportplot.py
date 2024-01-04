# Generated by Django 4.2.7 on 2024-01-04 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("a_plot", "0021_rename_commentt_likedcomment_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportPlot",
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
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("Off Topic", "Off Topic"),
                            ("Spam", "Spam"),
                            ("Sexual content", "Sexual content"),
                            ("Breaks Rules", "Breaks Rules"),
                            ("Other", "Other"),
                        ],
                        default="Off Topic",
                        max_length=100,
                    ),
                ),
                ("report_count", models.IntegerField(default=1)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(default="pending", max_length=100)),
                (
                    "plot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="a_plot.plot"
                    ),
                ),
                (
                    "reported_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]