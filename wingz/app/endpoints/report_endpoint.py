from rest_framework import permissions
from django.db.models import (
    F,
    ExpressionWrapper,
    DurationField,
    Count,
    OuterRef,
    Value,
    CharField,
)
from django.db.models.functions import ExtractMonth, ExtractYear, Concat, Cast
from .viewsets import BaseViewSet
from app.models import RideEvent
from .permissions import AdminPermission


class ReportAPI(BaseViewSet):
    permission_classes = (
        permissions.IsAuthenticated,
        AdminPermission,
    )
    queryset = RideEvent.objects.all()

    def list(self, request):
        reports = (
            RideEvent.objects.filter(description="Status changed to pickup")
            .annotate(
                dropoff_time=RideEvent.objects.filter(
                    ride_id=OuterRef("ride"),
                    ride__driver=OuterRef("ride__driver"),
                    description="Status changed to dropoff",
                ).values("created_at")[:1],
            )
            .annotate(
                duration=ExpressionWrapper(
                    F("dropoff_time") - F("created_at"), output_field=DurationField()
                )
            )
            .filter(duration__gt="1 hour")
            .annotate(year=ExtractYear("created_at"), month=ExtractMonth("created_at"))
            .annotate(
                driver=Concat(
                    F("ride__driver__first_name"),
                    Value(" "),
                    F("ride__driver__last_name"),
                )
            )
            .annotate(
                date=Concat(
                    Cast(F("year"), CharField()),
                    Value("-"),
                    Cast(F("month"), CharField()),
                )
            )
            .values("date", "driver")
            .annotate(trip_count=Count("ride_id"))
            .order_by("month", "ride__driver")
        )

        return self.response_200({"reports": reports})
