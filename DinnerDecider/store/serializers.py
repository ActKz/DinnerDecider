from rest_framework import serializers
from .models import Store, StorePhoto

class StorePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePhoto
        fields = ('store_id', 'photos')

class StoreSerializer(serializers.ModelSerializer):
    photos = StorePhotoSerializer(many=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'address', 'phone', 'avg_price', 'provide_by', 'photos')
