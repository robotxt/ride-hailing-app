# Generated by Django 5.1.5 on 2025-01-20 05:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rideevent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ride",
            name="dropoff_latitude",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(-90.0),
                    django.core.validators.MaxValueValidator(90.0),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="ride",
            name="dropoff_longitude",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(-180.0),
                    django.core.validators.MaxValueValidator(180.0),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="ride",
            name="pickup_latitude",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(-90.0),
                    django.core.validators.MaxValueValidator(90.0),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="ride",
            name="pickup_longitude",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(-180.0),
                    django.core.validators.MaxValueValidator(180.0),
                ]
            ),
        ),
    ]
