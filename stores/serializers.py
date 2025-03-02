from rest_framework import serializers

from .models import Store, StoreTable

from categories.serializers import CategorySerializer

from .utils import base64_qr_code


class StoreTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreTable
        fields = '__all__'
        read_only_fields = ['deleted_on']

    def create(self, validated_data):
        store_data = StoreTable(**validated_data)
        store_data.qr_code_base64 = base64_qr_code(store_data)
        store_data.save()
        return store_data


class StoreSerializer(serializers.ModelSerializer):
    tables = StoreTableSerializer(many=True, source='storetable_set', read_only=True)
    categories = CategorySerializer(many=True, source='category_set', read_only=True)

    class Meta:
        model = Store
        fields = '__all__'
        include = ('tables', 'categories',)
        read_only_fields = ['deleted_on']
# class GenerateTableQRCodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StoreTable
#         fields = '__all__'
#         read_only_fields = ['deleted_on']
#
#     def update(self, instance, validated_data):
#         try:
#             validated_data['qr_code_base64'] = base64_qr_code(instance)
#         except Exception as e:
#             print(e)
#             pass
#         return super().update(instance, validated_data)
