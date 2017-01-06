from rest_framework import serializers
from .models import Store, StorePhoto, StoreType, Area

class StoreTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreType
        fields = ('id', 'name')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name')

class StorePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePhoto
        fields = ('store_id', 'photos')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'address', 'phone', 'avg_price', 'provider', 'tid', 'aid')

