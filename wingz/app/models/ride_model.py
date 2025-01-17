from django.db import models
from .user_model import User
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

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rider_rides")
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver_rides")
    pickup_latitude = models.DecimalField(
        max_digits=8, decimal_places=6, validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    pickup_longitude = models.DecimalField(
        max_digits=9, decimal_places=6, validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )
    dropoff_latitude = models.DecimalField(
        max_digits=8, decimal_places=6, validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    dropoff_longitude = models.DecimalField(
        max_digits=9, decimal_places=6, validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )
    pickup_time = models.DateTimeField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=None, null=False)
