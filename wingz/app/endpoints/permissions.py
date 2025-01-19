from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from app.models import User


class AdminPermission(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.role == User.ADMIN:
            return True
        return False
