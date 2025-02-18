from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import StoreApiView, StoreTableApiView


router = SimpleRouter()
router.register(r'store-table', StoreTableApiView, basename='store-table')
router.register(r'', StoreApiView, basename='store')


urlpatterns = [
    path('', include(router.urls)),
]
