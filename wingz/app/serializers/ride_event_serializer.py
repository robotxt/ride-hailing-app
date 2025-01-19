from rest_framework import serializers

from app.models import RideEvent


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = "__all__"
