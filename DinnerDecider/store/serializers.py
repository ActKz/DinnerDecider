from rest_framework import serializers
from .models import Store, StorePhoto, StoreType, Area

class StorePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePhoto
        fields = ('store_id', 'photos')

class StoreSerializer(serializers.ModelSerializer):
    photos = StorePhotoSerializer(many=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'address', 'phone', 'avg_price', 'provide_by', 'photos', 'tid', 'aid')

class StoreTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreType
        fields = ('id', 'type')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'area')
