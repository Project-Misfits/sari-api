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
    filterset_fields = ['categories__name']

    queryset = Product.objects.filter(deleted_on=None)

    def destroy(self, request, *args, **kwargs):
        qs = self.get_object()
        qs.deleted_on = timezone.now()
        qs.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
