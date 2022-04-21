from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products
from .serializers import ProductsSerializer

class ProductView(APIView):
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        qs = Products.objects.all()
        serialized_data = ProductsSerializer(qs, many=True)
        return Response(serialized_data.data)
    
    def post(self, request, *args, **kwargs):
        pass