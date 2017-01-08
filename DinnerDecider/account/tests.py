from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from  .models import UserFavList, UserFavListName
from store.models import Store, StoreType, Area
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate

class UserFavListTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('foo','foo@cc.com','bar')
        cls.listA = UserFavListName.objects.create(listname="真難吃", uid=cls.user)
        cls.listB = UserFavListName.objects.create(listname="真好吃", uid=cls.user)
        cls.type = StoreType.objects.create(name="FOOD")
        cls.area = Area.objects.create(name='area')
        cls.storeA = Store.objects.create(name='A',address='A',phone='A',avg_price=6,provide_by=cls.user.username,type=cls.type,area=cls.area)
        cls.storeB = Store.objects.create(name='B',address='B',phone='B',avg_price=66,provide_by=cls.user.username,type=cls.type,area=cls.area)
        cls.storeC = Store.objects.create(name='C',address='C',phone='C',avg_price=666,provide_by=cls.user.username,type=cls.type,area=cls.area)
        cls.listA_a = UserFavList.objects.create(uid=cls.user, name=cls.listA, sid=cls.storeA)
        pass
    def setUp(self):
        self.client.force_authenticate(user=self.user)
        pass
    def test_add_favlist(self):
        data1 = {'sid':[2, 3 ], 'listname_id':1}
        data2 = {'sid':[1, 2, 3], 'listname_id': 2}
        self.assertEqual(UserFavList.objects.filter(name=self.listA).count(), 1)
        response = self.client.post('/favlist/add/', data1, format='json')
        self.assertEqual(UserFavList.objects.filter(name=self.listA).count(), 3)
        self.assertEqual(UserFavList.objects.filter(name=self.listB).count(), 0)
        response = self.client.post('/favlist/add/', data2, format='json')
        self.assertEqual(UserFavList.objects.filter(name=self.listB).count(), 3)
        pass
    def test_update_favlist(self):
        pass
    def test_get_favlist(self):
        response = self.client.get('/favlist/get/')
        self.assertEqual(response.data[0], {
            'listname_id': 1,
            'user': self.user.username,
            'listname': self.listA.listname,
            'storesData':[{
                'type': self.type.id,
                'favlistId': self.listA_a.id,
                'phone': self.storeA.phone,
                'provide_by': self.user.username,
                'type__name': self.type.name,
                'address': self.storeA.address,
                'area': self.area.id,
                'area__name': self.area.name,
                'name': self.storeA.name,
                'avg_price': self.storeA.avg_price,
                'id': self.storeA.id
                }]
            })
        pass
    def test_delete_favlist(self):
        response = self.client.delete('/favlist/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserFavList.objects.filter(name=self.listA).count(), 0)
        pass
    def test_not_authed_favlist(self):
        self.client.force_authenticate(user=None)
        data1 = {'sid':[2, 3 ], 'listname_id':1}
        response = self.client.post('/favlist/add/', data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.get('/favlist/get/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete('/favlist/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        pass

class UserFavListNameTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('foo','foo@cc.com','bar')
        cls.listname = UserFavListName.objects.create(listname="真難吃", uid=cls.user)
        pass
    def setUp(self):
        self.client.force_authenticate(user=self.user)
        pass
    def test_add_listname(self):
        data = {'listname': "真好吃"}
        response = self.client.post('/favlistname/add/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserFavListName.objects.count(), 2)
        pass
    def test_update_listname(self):
        data = {'listname': "真好好吃"}
        response = self.client.patch('/favlistname/1/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserFavListName.objects.get(pk=1).listname, data['listname'])
        pass
    def test_get_listname(self):
        data = {'listname':"真難吃"}
        response = self.client.get('/favlistname/get/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], {
            'listname': self.listname.listname,
            'id': self.listname.id
            })
        pass
    def test_delete_listname(self):
        response = self.client.delete('/favlistname/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserFavListName.objects.count(), 0)
        pass
    def test_not_authed_listname(self):
        self.client.force_authenticate(user=None)
        data = {'listname': "真好好吃"}
        response = self.client.post('/favlistname/add/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.patch('/favlistname/1/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete('/favlistname/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        pass

class UserTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('foo','foo@cc.com','bar')
        pass
    def setUp(self):
        self.client.force_authenticate(user=self.user)
        pass
    def test_add_user(self):
        self.client.force_authenticate(user=None)
        data = {'username': 'bar', 'email':'bar@cc.com', 'password': 'foo'}
        response = self.client.post('/users/create-account/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(authenticate(username='bar', password='foo') is not None)
        pass
    def test_get_user(self):
        response = self.client.get('/users/user-info/')
        user = User.objects.filter(username=self.user.username).values('last_login','username','email','date_joined').get()
        self.assertDictEqual(response.data[0], {
            'username': self.user.username,
            'email': self.user.email,
            'last_login': self.user.last_login,
            'date_joined': self.user.date_joined,
            })
        pass
    def test_update_password(self):
        data = {'password': 'foo'}
        response = self.client.post('/users/change-password/',data,format='json')
        self.assertTrue(authenticate(username='foo', password='foo') is not None)
        pass
    def test_update_email(self):
        data = {'email': 'bar@cc.com'}
        response = self.client.post('/users/change-email/', data, format='json')
        self.assertEqual(User.objects.get(pk=1).email, data['email'])
        pass
    def test_not_authed_user(self):
        self.client.force_authenticate(user=None)
        data = {'password': 'foo'}
        response = self.client.post('/users/change-password/',data,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        data = {'email': 'bar@cc.com'}
        response = self.client.post('/users/change-email/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        pass
