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
from .models import UserFavList, UserFavListName
from store.models import Store

class UserFavListNameViewSet(viewsets.ViewSet):
    queryset = UserFavListName.objects.all()

    @list_route(methods=['get'], permission_classes=[permissions.IsAuthenticated], url_path='get')
    def list_listname(self, request):
        return Response(self.queryset.filter(uid=request.user).values())

    @list_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='add')
    def create_listname(self, request):
        if 'listname' in request.data:
            uid = User.objects.filter(username=request.user.username).get()
            self.queryset.create(listname=request.data['listname'],uid=uid)
            return Response("Success")
        return Response("Fail",status=400)

    @detail_route(methods=['patch'], permission_classes=[permissions.IsAuthenticated], url_path='update')
    def update_listname(self, request, pk=None):
        if pk == None:
            return Response("Primary key mus be given in url", status=400)
        if 'listname' in request.data:
            p = self.queryset.filter(id=pk).update(listname=request.data['listname'])
            if p > 0:
                return Response("Success")
            else:
                return Response("Update fail",status=400)
        return Response("Some field are not provided",status=400)

    @detail_route(methods=['delete'], permission_classes=[permissions.IsAuthenticated], url_path='delete')
    def delete_listname(self, request, pk=None):
        if pk == None:
            return Response("Primary key mus be given in url", status=400)
        obj = self.queryset.get(pk=pk)
        if obj != None:
            obj.delete()
            return Response("Success")
        else:
            return Response("List does not exist",status=400)


class UserFavListViewSet(viewsets.ViewSet):
    queryset = UserFavList.objects.all()
    fields = ('listname_id', 'favlist_id', 'sid')

    @list_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='add')
    def create_favlist(self, request):
        if all(key in request.data for key in ('listname_id','sid')):
            uid = User.objects.filter(username=request.user.username).get()
            sid = Store.objects.filter(id=request.data['sid']).get()
            listname = UserFavListName.objects.filter(pk=request.data['listname_id']).get()
            p = self.queryset.create(uid=uid, sid=sid, name=listname)
            if p != None:
                return Response("Success")
            else:
                return Response("Create fail",status=400)
        else:
            return Response("Some field are not provided",status=400)

    @list_route(methods=['get'], permission_classes=[permissions.IsAuthenticated], url_path='get')
    def list_favlist(self, request):
        res = self.queryset.filter(uid__username=request.user.username).values('sid__name','sid__address','sid__phone','sid__provide_by','sid__avg_price','sid__type','sid__type__name','sid__area','sid__area__name','sid__id','name__listname','uid__username','id')
        return Response(res)

    @detail_route(methods=['delete'], permission_classes=[permissions.IsAuthenticated], url_path='delete')
    def delete_favlist(self, request, pk=None):
        if pk == None:
            return Response("Primary key mus be given in url", status=400)
        obj = self.queryset.get(pk=pk)
        if obj != None:
            obj.delete()
            return Response("Success")
        else:
            return Response("List does not exist",status=400)

    @detail_route(methods=['patch'], permission_classes=[permissions.IsAuthenticated], url_path='update')
    def update_favlist(self, request, pk=None):

        if pk == None:
            return Response("Primary key mus be given in url", status=400)
        if all(key in request.data for key in self.fields):
            obj = self.queryset.filter(pk=pk).update(name=request.data['listname_id'])
            if obj > 0:
                return Response("Success")
            else:
                return Response("List does not exist",status=400)
        else:
            return Response("Some field are not provided",status=400)

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

