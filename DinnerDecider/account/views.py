from django.shortcuts import render

# Create your views here.
#from account.models import User
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from account.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.core.validators import *
from django.core.exceptions import ValidationError


class UserViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.values('username','email')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request):
        return Response(self.queryset)
    def create(self, request):
        req = request.data
        if req['username'] == "":
            return Response("Empty username",status=400)
        if req['password'] == "":
            return Response("Empty password",status=400)
        try:
            validate_email(req['email'])
        except ValidationError:
            return Response("Invalid email",status=400)
        user = User.objects.create_user(req['username'],req['email'],req['password'])
        user.save()
        return Response("Create success", status=200)

    def retrieve(self, request, pk=None):
        return Response(self.queryset.filter(username=request.user))

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

#@api_view(['POST'])
#def login(request):
#    print(request)
#    return Response(request)

