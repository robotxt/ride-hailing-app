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
        items = self.get_queryset()
        page = self.paginate_queryset(items)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
