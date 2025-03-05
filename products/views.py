from django_filters.rest_framework import DjangoFilterBackend

from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer


class ProductApiView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories__name', 'store']

    # This forces the api to use store id else it will return an empty result.
    # In the future, we can update the return if no store id to all products
    def get_queryset(self, *args, **kwargs):
        store_id = self.request.query_params.get('store', None)
        print(store_id)
        if store_id:
            return Product.objects.filter(store=store_id, deleted_on=None)
        return Product.objects.none()

    def destroy(self, request, *args, **kwargs):
        qs = self.get_object()
        qs.deleted_on = timezone.now()
        qs.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
