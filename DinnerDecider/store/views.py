from django.shortcuts import render
from rest_framework import viewsets, serializers, permissions
from .models import Store, StoreType, Area
from .serializers import StoreTypeSerializer, AreaSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django.db.models.query_utils import Q
from django.forms.models import model_to_dict


class StoreViewSet(viewsets.ViewSet):
    queryset = Store.objects.all()
    fields = ('name','address','phone','provide_by','avg_price','type','type__name','area','area__name')

    @list_route(methods=['get'], url_path='get')
    def store_info(self, request ):
        if 'id' in request.query_params:
            obj = self.queryset.filter(id=request.query_params['id']).values('name','address','phone','provide_by','avg_price','type','type__name','area','area__name','id','image_url')
            if obj != None:
                return Response(obj)
            else:
                return Response("No such store",status=400)
        else:
            return Response("Primary key must be given in query",status=400)


    @list_route(methods=['get'], url_path='list')
    def list_store(self, request):
        r = request.query_params
        if 'keyword' in r:
            res = Store.objects.values('name','address','phone','provide_by','avg_price','type','type__name','area','area__name','id','image_url').filter(Q(name__icontains=r['keyword']) |
                    Q(address__icontains=r['keyword']) |
                    Q(phone__icontains=r['keyword']) |
                    Q(provide_by__icontains=r['keyword']) |
                    Q(type__name__icontains=r['keyword']) |
                    Q(area__name__icontains=r['keyword']) )
        else:
            res = Store.objects.values('name','address','phone','provide_by','avg_price','type','type__name','area','area__name','id','image_url')
        return Response(res)

    @list_route(methods=['post'], url_path='add', permission_classes=[permissions.IsAuthenticated])
    def add_store(self, request):
        data = request.data
        fields = ('name', 'address', 'phone', 'avg_price', 'tid', 'aid')
        if all(key in data for key in fields):
            type = StoreType.objects.get(pk=data['tid'])
            area = Area.objects.get(pk=data['aid'])
            if not 'image_url' in data:
                data['image_url'] = None
            store = Store(
                    name = data['name'],
                    address = data['address'],
                    phone = data['phone'],
                    avg_price = data['avg_price'],
                    provide_by = request.user.username,
                    type = type,
                    area = area,
                    image_url = data['image_url'],
                    )
            store.save()
            return Response("Success")
        else:
            return Response("Fail",status=400)

    @detail_route(methods=['patch'], url_path='update', permission_classes=[permissions.IsAuthenticated])
    def update_store(self, request, pk=None):
        if pk == None:
            return Response("Primary key must be given in query",status=400)
        else:
            data = request.data
            fields = ('name', 'address', 'phone', 'avg_price', 'tid', 'aid')
            if all(key in data for key in fields):
                type = StoreType.objects.get(pk=data['tid'])
                area = Area.objects.get(pk=data['aid'])
                if not 'image_url' in data:
                    data['image_url'] = None
                store = Store(
                        id = pk,
                        name = data['name'],
                        address = data['address'],
                        phone = data['phone'],
                        avg_price = data['avg_price'],
                        provide_by = request.user.username,
                        type = type,
                        area = area,
                        image_url = data['image_url']
                        )
                store.save()
                return Response("Success")
            else:
                return Response("Some fields are not given",status=400)

    @detail_route(methods=['delete'], url_path='delete', permission_classes=[permissions.IsAuthenticated])
    def delete_store(self, request, pk=None):
        if pk == None:
            return Response("Primary key must be given in query",status=400)
        obj = self.queryset.get(pk=pk)
        if obj != None:
            obj.delete()
            return Response("Success")
        else:
            return Response("Fail",status=400)


class StoreTypeViewSet(viewsets.ModelViewSet):
    queryset = StoreType.objects.all()
    serializer_class = StoreTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#class StorePhotoViewSet(viewsets.ModelViewSet):
#    queryset = StorePhoto.objects.all()
#    serializer_class = StorePhotoSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SearchViewSet(viewsets.ViewSet):
    queryset = Store.objects.all()

    @list_route(methods=['get'], url_path='store')
    def fuzzy_search(self, request):
        if 'keyword' in request.query_params and request.query_params['keyword'] != "":
            res = self.queryset.filter(Q(name__icontains=request.query_params['keyword']) |
                                       Q(address__icontains=request.query_params['keyword']) |
                                       Q(phone__icontains=request.query_params['keyword']) |
                                       Q(provide_by__icontains=request.query_params['keyword'])).values()
            return Response(res)
        else:
            res = self.queryset.select_related('tid','aid').values()
            return Response(Store.objects.prefetch_related('tid_id').values())

    @list_route(methods=['get'], url_path='type')
    def type_search(self, request):
        if 'tid' in request.query_params and request.query_params['tid'].isdecimal():
            res = self.queryset.filter(tid__exact=request.query_params['tid']).values()
            return Response(res)
        else:
            return Response("Invalid tid", status=400)

    @list_route(methods=['get'], url_path='area')
    def area_search(self, request):
        if 'aid' in request.query_params and request.query_params['aid'].isdecimal():
            res = self.queryset.filter(aid__exact=request.query_params['aid']).values()
            return Response(res)
        else:
            return Response("Invalid aid", status=400)

    @list_route(methods=['get'], url_path='type-area-search')
    def type_area_search(self, request):
        r = request.query_params
        if 'aid' in r and 'tid' in r and r['aid'].isdecimal() and r['tid'].isdecimal():
            res = self.queryset.filter(aid__exact=request.query_params['aid'],tid__exact=request.query_params['tid']).values()
            return Response(res)
        else:
            return Response("Invalid tid or aid", status=400)

    @list_route(methods=['get'], url_path='price-limit')
    def price_limit(self, request):
        r = request.query_params
        if 'llim' in r and 'ulim' in r and r['llim'].isdecimal() and r['ulim'].isdecimal():
            res = self.queryset.filter(avg_price__range=(request.query_params['llim'],request.query_params['ulim'])).values()
            return Response(res)
        else:
            return Response("Invalid price", status=400)
