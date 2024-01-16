# Generated by Django 5.0.1 on 2024-01-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cost",
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
                ("category", models.TextField()),
                ("amount", models.IntegerField()),
                ("date", models.DateField()),
                ("file", models.FileField(upload_to="")),
            ],
        ),
    ]
