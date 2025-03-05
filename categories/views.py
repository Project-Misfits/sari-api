from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategorySerializer


class CategoryApiView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        store_id = self.request.query_params.get('store', None)
        if store_id:
            return Category.objects.filter(store=store_id, deleted_on=None)
        return Category.objects.none()

    def destroy(self, request, *args, **kwargs):
        qs = self.get_object()
        qs.deleted_on = timezone.now()
        qs.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
