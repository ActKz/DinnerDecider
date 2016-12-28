from django.shortcuts import render

# Create your views here.
#from account.models import User
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, authentication
from account.serializers import UserSerializer, PasswordSerializer
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.request import Request
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.values('username','email')
    serializer_class = UserSerializer
#   permission_classes = (permissions.IsAuthenticated,)
    def get_serializer_class(self):
        return self.serializer_class

    @list_route(methods=['get'], permission_classes=[permissions.IsAuthenticatedOrReadOnly], url_path='user-info')
    def user_info(self, request):
        """
        Need auth

        ---

        No required field
        """
#       return Response(self.queryset)
        return Response(self.queryset.filter(username=request.user))

    @list_route(methods=['post'], url_path='create-account')
    def create_account(self, request):
        """


        ---

        Required field:
        - username
        - email
        - password
        """
        filter_fields = ('username', 'email', 'password','shit')
        if request.user.is_authenticated:
            return Response("Already login")
        req = request.data
        if req['username'] == "":
            return Response("Empty username",status=400)
        if req['password'] == "":
            return Response("Empty password",status=400)
        try:
            validate_email(req['email'])
        except ValidationError:
            return Response("Invalid email",status=400)
        try:
            user = User.objects.create_user(req['username'],req['email'],req['password'])
        except IntegrityError:
            return Response("Account exist", status=400)
        user.save()
        return Response("Create success", status=200)


    #Change password
    @list_route(methods=['post'],permission_classes=[permissions.IsAuthenticatedOrReadOnly], url_path='change-password')
    def change_password(self, request):
        """
        Need auth

        ---

        Required field:
        - password
        """
        req = request.data
        if req['password'] == "":
            return Response("Empty password", status=400)
        user = User.objects.get(username=request.user)
        if user != None:
            user.set_password(req['password'])
            user.save()
            return Response("Update success")
        else:
            return Response("No such user")

    #Change email
    @list_route(methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly], url_path='change-email')
    def change_email(self, request):
        """
        Need auth

        ---

        Required field:
        - email
        """
        req = request.data
        try:
            validate_email(req['email'])
        except ValidationError:
            return Response("Invalid email", status=400)
        user = User.objects.get(username=request.user)
        if user != None:
            user.email = req['email']
            user.save()
            return Response("Update success")
        else:
            return Response("No such user")
    @list_route(methods=['post'],permission_classes=[permissions.IsAuthenticatedOrReadOnly], url_path='delete-account')
    def destroy_account(self, request):
        """
        Unavailable now

        ---

        Need auth

        ---

        Required field:
        - username
        """
        return Response("Not allowed",status=400)

