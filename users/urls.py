from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TokenObtainPairView, RegisterApiView

router = DefaultRouter

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterApiView.as_view({'post': 'create'}), name='register'),
]
