from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .viewsets import BaseViewSet
from app.serializers import LoginSerializer


class LoginAPI(BaseViewSet):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def create(self, request, pk=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return self.response_200({"token": token.key})

        return self.response_400(serializer)
