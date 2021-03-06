# Generated by Django 3.2.4 on 2022-03-01 13:48

from django.db import migrations, models
import plant_disease_detection.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageModel",
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
                    "image",
                    models.ImageField(
                        blank=True, upload_to=plant_disease_detection.models.upload_path
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
