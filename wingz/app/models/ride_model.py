from django.db import models
from app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Ride(models.Model):
    EN_ROUTE = "EN_ROUTE"
    PICKUP = "PICKUP"
    DROPOFF = "DROPOFF"
    STATUS_CHOICES = [
        (EN_ROUTE, "en-route"),
        (PICKUP, "pickup"),
        (DROPOFF, "dropoff"),
    ]

    rider = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rider_rides"
    )
    driver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="driver_rides"
    )
    pickup_latitude = models.FloatField(
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    pickup_longitude = models.FloatField(
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )
    dropoff_latitude = models.FloatField(
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    dropoff_longitude = models.FloatField(
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )
    pickup_time = models.DateTimeField()
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default=None, null=False
    )
