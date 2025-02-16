from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (
    CustomTokenObtainPairSerializer, RegistrationSerializer, CustomUserDetailSerializer
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


class UserDetailsApiView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserDetailSerializer

    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        try:
            qs = User.objects.get(id=request.user.id)
            _serializer = CustomUserDetailSerializer(qs)
            return Response(_serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)