import datetime
from django.utils import timezone
from rest_framework import serializers

from .ride_event_serializer import RideEventSerializer
from app.models import Ride


class RideSerializer(serializers.ModelSerializer):
    todays_ride_events = serializers.SerializerMethodField(read_only=True)

    def get_todays_ride_events(self, obj: Ride):
        now_date = timezone.now()
        pass_24hr = now_date - datetime.timedelta(hours=24)
        events = obj.events.filter(created_at__range=(pass_24hr, now_date))
        serialize = RideEventSerializer(events, many=True)
        return serialize.data

    class Meta:
        model = Ride
        fields = "__all__"
