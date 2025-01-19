from rest_framework import serializers

from .ride_event_serializer import RideEventSerializer
from app.models import Ride


class RideSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField(read_only=True)

    def get_events(self, obj: Ride):
        events = obj.events.all()
        serialize = RideEventSerializer(events, many=True)
        return serialize.data

    class Meta:
        model = Ride
        fields = "__all__"
