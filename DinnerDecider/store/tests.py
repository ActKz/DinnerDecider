from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from  .models import Store, StoreType, Area
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

class AreaTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('foo')
        cls.area = Area.objects.create(name="台北市")
        pass
    def setUp(self):
        self.client.force_authenticate(user=self.user)
        pass
    def test_add_area(self):
        data = {'name':'新北市'}
        response = self.client.post('/area/',data,format='json')
        self.assertEqual(Area.objects.count(), 2)
        self.assertEqual(Area.objects.get(pk=2).name, data['name'])
        pass
    def test_delete_area(self):
        response = self.client.delete('/area/1/')
        self.assertEqual(Area.objects.count(), 0)
        pass
    def test_get_area(self):
        response = self.client.get('/area/')
        self.assertEqual(response.data[0], model_to_dict(self.area))
        pass
    def test_not_authed_area(self):
        self.client.force_authenticate(user=None)
        data = {'name':'新北市'}
        response = self.client.post('/area/',data,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete('/area/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        pass


class StoreTypeTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('foo')
        cls.type = StoreType.objects.create(name="牛排")
        pass
    def setUp(self):
        self.client.force_authenticate(user=self.user)
        pass
    def test_add_type(self):
        data = {'name':'豬排'}
        response = self.client.post('/storetype/', data, format='json')
        self.assertEqual(StoreType.objects.count(), 2)
        self.assertEqual(StoreType.objects.get(pk=2).name, data['name'])
        pass
    def test_delete_type(self):
        response = self.client.delete('/storetype/1/')
        self.assertEqual(StoreType.objects.count(), 0)
        pass
    def test_get_type(self):
        response = self.client.get('/storetype/')
        self.assertDictEqual(response.data[0], model_to_dict(self.type))
        pass
    def test_not_authed_type(self):
        self.client.force_authenticate(user=None)
        data = {'name':'豬排'}
        response = self.client.post('/storetype/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete('/storetype/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        pass

class StoreTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.type = StoreType.objects.create(name="漢堡")
        cls.area = Area.objects.create(name="海底")
        cls.user = User.objects.create_user('foo')
        cls.store = Store.objects.create(name="蟹堡王",address="海之霸對面",phone="7777",avg_price=9487,type=cls.type,area=cls.area,provide_by=cls.user.username)

        cls.url = {'add':'/stores/add/','get':'/stores/get/','list':'/stores/list/'}
        pass

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        pass

    def test_add_store(self):
        # create success
        data = {"name": "海霸王", "address": "霸王街", "phone": "8888888", "avg_price": 888, "tid": "1", "aid": "1",}
        response = self.client.post(self.url['add'], data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Store.objects.count(), 2, msg="Add second store succeeds")
        self.assertEqual(Store.objects.get(pk=2).name, data['name'])
        self.assertEqual(Store.objects.get(pk=2).address, data['address'])
        self.assertEqual(Store.objects.get(pk=2).phone, data['phone'])
        self.assertEqual(Store.objects.get(pk=2).avg_price, data['avg_price'])
        self.assertEqual(Store.objects.get(pk=2).type, self.type)
        self.assertEqual(Store.objects.get(pk=2).area, self.area)
        # create fail
        data = {"name": "海霸王", "phone": "8888888", "avg_price": 888, "tid": "1", "aid": "1",}
        response = self.client.post(self.url['add'], data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_store(self):
        data = {"id": 1 }
        response = self.client.get(self.url['get']+"?id=1", format='json')
        self.assertDictEqual(dict(response.data[0]), dict({
            'name': self.store.name,
            'address': self.store.address,
            'phone': self.store.phone,
            'avg_price': self.store.avg_price,
            'provide_by': self.store.provide_by,
            'type': self.type.id,
            'type__name': self.type.name,
            'area': self.area.id,
            'area__name': self.area.name,
            'id': self.store.id,
            'image_url': None
            }))

    def test_list_store(self):
        data = "?keyword=螃蟹"
        response = self.client.get(self.url['list']+data, format='json')
        self.assertEqual(list(response.data), [])
        data = "?keyword=蟹堡"
        response = self.client.get(self.url['list']+data, format='json')
        self.assertDictEqual(dict(response.data[0]), dict({
            'name': self.store.name,
            'address': self.store.address,
            'phone': self.store.phone,
            'avg_price': self.store.avg_price,
            'provide_by': self.store.provide_by,
            'type': self.type.id,
            'type__name': self.type.name,
            'area': self.area.id,
            'area__name': self.area.name,
            'id': self.store.id,
            'image_url': None
            }))

    def test_delete_store(self):
        response = self.client.delete('/stores/1/delete/')
        self.assertEqual(Store.objects.count(), 0)

    def test_update_store(self):
        data = {"name": "海霸王", "address": "霸王路", "phone": "8888888", "avg_price": 888, "tid": "1", "aid": "1", "store_id": "1"}
        response = self.client.patch('/stores/1/update/', data, format='json')
        self.assertEqual(Store.objects.get(pk=1).address, "霸王路")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.patch('/stores/1/update/', {"name":"WTF"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_authed_store(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url['add'])
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete('/stores/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.patch('/stores/1/update/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


