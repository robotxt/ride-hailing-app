from rest_framework import serializers

from app.models import User


class LoginSerializer(serializers.Serializer):
    INVALID_LOGIN = "Invalid login credentials"

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data.get("email"))
        except User.DoesNotExist:
            raise serializers.ValidationError(self.INVALID_LOGIN)

        if not user.check_password(data.get("password")):
            raise serializers.ValidationError(self.INVALID_LOGIN)

        data["user"] = user
        return data
