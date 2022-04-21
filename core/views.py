from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Products
from .serializers import ProductsSerializer


class ProductList(APIView):
    serializer_class = ProductsSerializer
    """
        get: List all products, to do: add pagination in the future
    """
    def get(self, request, format=None):
        qs = Products.objects.all()
        serialized_data = ProductsSerializer(qs, many=True)
        return Response(serialized_data.data)
    """
        post: add new product
    """
    def post(self, request, format=None):
        data = request.data
        serialized_data = ProductsSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsDetail(APIView):
    serializer_class = ProductsSerializer
    """
        get_objet: will do the querying if the product with pk exists

        get: get one product using pk

        put: update the product with pk

        delete: delete the product with pk, we can also disable it etc
    """
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        qs = self.get_object(pk)
        serialized_data = ProductsSerializer(qs)
        return Response(serialized_data.data)
    
    def put(self, request, pk, format=None):
        qs = self.get_object(pk)
        serialized_data = ProductsSerializer(qs, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        qs = self.get_object(pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)