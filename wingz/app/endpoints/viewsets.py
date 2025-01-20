from rest_framework import viewsets
from rest_framework import status, serializers
from rest_framework.response import Response


class BaseViewSet(viewsets.ViewSet):

    @staticmethod
    def _get_data(serializer):
        if isinstance(serializer, serializers.Serializer) or isinstance(
            serializer, serializers.ListSerializer
        ):
            return serializer.data
        return serializer

    @staticmethod
    def _get_errors(serializer):
        if isinstance(serializer, serializers.Serializer) or isinstance(
            serializer, serializers.ListSerializer
        ):
            return serializer.errors
        return serializer

    def response_200(self, serializer):
        return Response(self._get_data(serializer), status=status.HTTP_200_OK)

    def response_201(self, serializer):
        return Response(self._get_data(serializer), status=status.HTTP_201_CREATED)

    def response_400(self, serializer):
        return Response(
            self._get_errors(serializer), status=status.HTTP_400_BAD_REQUEST
        )
