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

        # Set default sort pickup_time to desc
        sort_pickup = "-pickup_time"
        if sort_pickup_time == "asc":
            sort_pickup = "pickup_time"

        items = self.get_queryset().order_by(sort_pickup)
        page = self.paginate_queryset(items)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
