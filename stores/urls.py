from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import StoreApiView, StoreTableApiView


router = SimpleRouter()
router.register(r'', StoreApiView, basename='store')
router.register(r'store-table', StoreTableApiView, basename='store-table')


urlpatterns = [
    path('', include(router.urls)),
]
