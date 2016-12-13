from django.db import models

# Create your models here.
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    avg_price = models.PositiveIntegerField()
    provide_by = models.CharField(max_length=15)


class StorePhoto(models.Model):
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    photos = models.ImageField()
