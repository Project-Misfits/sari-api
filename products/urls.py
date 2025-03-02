from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import ProductApiView

router = SimpleRouter()
router.register(r'', ProductApiView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
