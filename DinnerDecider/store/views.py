from django.shortcuts import render
from rest_framework import viewsets, serializers, permissions
from .models import Store, StorePhoto, StoreType, Area
from .serializers import StoreSerializer, StoreTypeSerializer, AreaSerializer, StorePhotoSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = ()

class StoreTypeViewSet(viewsets.ModelViewSet):
    queryset = StoreType.objects.all()
    serializer_class = StoreTypeSerializer
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = ()

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = ()

class StorePhotoViewSet(viewsets.ModelViewSet):
    queryset = StorePhoto.objects.all()
    serializer_class = StorePhotoSerializer
#   permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = ()
