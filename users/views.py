from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    CustomTokenObtainPairSerializer, RegistrationSerializer
)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: CustomTokenObtainPairSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    http_method_names = ['post', 'option']

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: RegistrationSerializer,
        }
    )
    def create(self, request, *args, **kwargs):
        _serializer = self.serializer_class(data=request.data)
        if _serializer.is_valid():
            self.perform_create(_serializer)
            headers = self.get_success_headers(_serializer.data)

            return Response(data=_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()
