from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Store
from .serializers import StoreSerializer, StoreTableSerializer


class StoreApiView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer

    queryset = Store.objects.filter(deleted_on=None)

    def destroy(self, request, *args, **kwargs):
        qs = self.get_object()
        qs.deleted_on = timezone.now()
        qs.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreTableApiView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreTableSerializer

    queryset = Store.objects.filter(deleted_on=None)

    def destroy(self, request, *args, **kwargs):
        qs = self.get_object()
        qs.deleted_on = timezone.now()
        qs.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
