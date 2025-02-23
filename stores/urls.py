from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import StoreApiView, StoreTableApiView, GenerateTableQRCodeApiView


router = SimpleRouter()
router.register(r'store-table', StoreTableApiView, basename='store-table')
# router.register(r'store-table/qr/generate', GenerateTableQRCodeApiView, basename='generate-table-qr')
router.register(r'', StoreApiView, basename='store')


urlpatterns = [
    path('', include(router.urls)),
    path('store-table/qr/generate', GenerateTableQRCodeApiView.as_view({'patch': 'update'}))
]
