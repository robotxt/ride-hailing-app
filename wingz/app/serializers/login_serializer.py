from rest_framework import serializers

from app.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data.get("email"))
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")

        if not user.check_password(data.get("password")):
            raise serializers.ValidationError("Invalid login credentials")

        data["user"] = user
        return data
