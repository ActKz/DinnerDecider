from django.shortcuts import render

# Create your views here.
#from account.models import User
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, authentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.request import Request
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import generics
from django.contrib.auth import logout as Logout
from .models import UserFavList


#class UserFavListViewSet(viewsets.ViewSet):
#    queryset = UserFavList.objects.all()

class UserViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()

    @list_route(methods=['get'], permission_classes=[permissions.IsAuthenticated], url_path='user-info')
    def user_info(self, request):
        res = self.queryset.filter(username=request.user.username).values('last_login','username','email','date_joined')
        return Response(res)

    @list_route(methods=['post'], url_path='create-account')
    def create_account(self, request):
        if request.user.is_authenticated:
            return Response("Already login",status=400)
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
    @list_route(methods=['post'],permission_classes=[permissions.IsAuthenticated], url_path='change-password')
    def change_password(self, request):
        req = request.data
        if req['password'] == "":
            return Response("Empty password", status=400)
        user = User.objects.get(username=request.user)
        if user != None:
            user.set_password(req['password'])
            user.save()
            return Response("Update success")
        else:
            return Response("No such user",status=400)

    #Change email
    @list_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='change-email')
    def change_email(self, request):
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
            return Response("No such user",status=400)
    @list_route(methods=['get'],permission_classes=[permissions.IsAuthenticated], url_path='delete-account')
    def destroy_account(self, request):
        return Response("Not allowed",status=200)

    @list_route(methods=['get'], permission_classes=[permissions.IsAuthenticated], url_path='logout')
    def logout(self, request):
        Logout(request)
        return Response("logout success")

