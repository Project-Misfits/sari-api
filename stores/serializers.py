from rest_framework import serializers

from .models import Store, StoreTable


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ['deleted_on']


class StoreTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreTable
        fields = '__all__'
        read_only_fields = ['deleted_on']
