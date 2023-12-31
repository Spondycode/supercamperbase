# Generated by Django 4.2.7 on 2023-12-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_plot", "0014_plot_countries"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plot",
            name="country",
        ),
        migrations.AlterField(
            model_name="plot",
            name="countries",
            field=models.CharField(
                choices=[
                    ("United Kingdom", "United Kingdom"),
                    ("France", "France"),
                    ("Spain", "Spain"),
                    ("Portugal", "Portugal"),
                    ("Italy", "Italy"),
                    ("Germany", "Germany"),
                    ("Netherlands", "Netherlands"),
                    ("Ireland", "Ireland"),
                    ("Belgium", "Belgium"),
                    ("Greece", "Greece"),
                    ("Switzerland", "Switzerland"),
                    ("Austria", "Austria"),
                    ("Sweden", "Sweden"),
                    ("Norway", "Norway"),
                    ("Finland", "Finland"),
                    ("Denmark", "Denmark"),
                    ("Croatia", "Croatia"),
                    ("Poland", "Poland"),
                    ("Romania", "Romania"),
                    ("Bulgaria", "Bulgaria"),
                    ("Czech Republic", "Czech Republic"),
                    ("Hungary", "Hungary"),
                    ("Slovakia", "Slovakia"),
                    ("Slovenia", "Slovenia"),
                    ("Luxembourg", "Luxembourg"),
                    ("Latvia", "Latvia"),
                    ("Estonia", "Estonia"),
                    ("Lithuania", "Lithuania"),
                    ("Malta", "Malta"),
                    ("Cyprus", "Cyprus"),
                    ("Iceland", "Iceland"),
                    ("Liechtenstein", "Liechtenstein"),
                    ("Monaco", "Monaco"),
                    ("San Marino", "San Marino"),
                    ("Andorra", "Andorra"),
                    ("Albania", "Albania"),
                    ("Armenia", "Armenia"),
                    ("Azerbaijan", "Azerbaijan"),
                    ("Belarus", "Belarus"),
                    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
                    ("Georgia", "Georgia"),
                    ("Kazakhstan", "Kazakhstan"),
                    ("Kosovo", "Kosovo"),
                    ("Macedonia", "Macedonia"),
                    ("Moldova", "Moldova"),
                    ("Montenegro", "Montenegro"),
                    ("Russia", "Russia"),
                    ("Serbia", "Serbia"),
                    ("Turkey", "Turkey"),
                    ("Ukraine", "Ukraine"),
                ],
                default="Spain",
                max_length=100,
            ),
        ),
    ]
