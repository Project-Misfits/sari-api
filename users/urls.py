from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterApiView, TokenObtainPairView

router = DefaultRouter()
# router.register('register', RegisterApiView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
