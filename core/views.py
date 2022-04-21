from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Products
from .serializers import ProductsSerializer


class ProductView(APIView):
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        qs = Products.objects.all()
        serialized_data = ProductsSerializer(qs, many=True)
        return Response(serialized_data.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serialized_data = ProductsSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)