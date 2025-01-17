from django.db import models
from .ride_model import Ride


class RideEvent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="events")
    description = models.TextField()
