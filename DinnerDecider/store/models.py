from django.db import models

class StorePhoto(models.Model):
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    photos = models.URLField()

class StoreType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    avg_price = models.PositiveIntegerField()
    provide_by = models.CharField(max_length=15)
    type = models.ForeignKey('StoreType', null=True, on_delete=models.SET_NULL)
    area = models.ForeignKey('Area', null=True, on_delete=models.SET_NULL)


