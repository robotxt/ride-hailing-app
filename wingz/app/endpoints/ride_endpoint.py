from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.db.models import F, Func
from django.contrib.gis.db.models import PointField
from .viewsets import BaseViewSet
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from .permissions import AdminPermission
from app.serializers import RideSerializer
from app.models import Ride


class RideAPI(BaseViewSet, GenericViewSet):
    serializer_class = RideSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        AdminPermission,
    )
    queryset = Ride.objects.all()

    def list(self, request):
        sort_pickup_time = request.query_params.get("sort-pickup-time", "desc")
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")

        # Set default sort pickup_time to desc
        sort_pickup = "-pickup_time"
        if sort_pickup_time == "asc":
            sort_pickup = "pickup_time"

        items = self.get_queryset()
        items = items.order_by(sort_pickup)

        if latitude and longitude:
            query_location = Point(float(longitude), float(latitude), srid=4326)
            items = items.annotate(
                distance=Distance(
                    query_location,
                    Func(
                        F("pickup_longitude"),
                        F("pickup_latitude"),
                        function="ST_MakePoint",
                        output_field=PointField(srid=4326),
                    ),
                ),
            ).order_by(
                "distance"
            )  # Sort: by closest distance

        page = self.paginate_queryset(items)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
