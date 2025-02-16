from django.urls import path

from .views import TokenObtainPairView, RegisterApiView, UserDetailsApiView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterApiView.as_view({'post': 'create'}), name='register'),
    path('detials/', UserDetailsApiView.as_view({'get': 'list'}), name='user-details'),
]
