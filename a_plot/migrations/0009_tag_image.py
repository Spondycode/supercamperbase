# Generated by Django 4.2.7 on 2023-12-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_plot", "0008_remove_plot_tags_plot_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="icons/"),
        ),
    ]