from django.shortcuts import render
from rest_framework import viewsets, serializers, permissions
from .models import Store, StorePhoto
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
