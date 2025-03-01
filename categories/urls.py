from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import CategoryApiView

router = SimpleRouter()
router.register(r'', CategoryApiView, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
