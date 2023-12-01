# Generated by Django 4.2.7 on 2023-11-30 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Plot",
            fields=[
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("image", models.URLField(blank=True, null=True)),
                ("plot", models.CharField(max_length=100)),
                ("campsite", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("list_date", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="plots",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
