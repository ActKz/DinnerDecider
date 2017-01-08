from django.db import models
from store.models import Store
from django.contrib.auth.models import User


class UserFavListName(models.Model):
    uid = models.ForeignKey(User, on_delete = models.CASCADE)
    listname = models.CharField(max_length=40)

class UserFavList(models.Model):
    uid = models.ForeignKey(User, on_delete = models.CASCADE)
    sid = models.ForeignKey('store.Store', on_delete = models.CASCADE)
    name = models.ForeignKey('UserFavListName', on_delete= models.CASCADE)

