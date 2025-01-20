from django.db import models
from .ride_model import Ride


class RideEvent(models.Model):
    ENROUTE = "Status changed to en-route"
    PICKUP_DESC = "Status changed to pickup"
    DROPOFF_DESC = "Status changed to dropoff"

    created_at = models.DateTimeField(auto_now_add=True)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="events")
    description = models.TextField()
