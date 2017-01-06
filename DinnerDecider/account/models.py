from django.db import models
from store.models import Store
from django.contrib.auth.models import User
from store.models import Store

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#class UserFavList(models.Model):
#    uid = models.ForeignKey('User', on_delete = models.CASCADE)
#    sid = models.ForeignKey('Store', on_delete = models.CASCADE)
#    listname = models.CharField(max_length=40)
#class UserManager(BaseUserManager):
#   def create_user(self, username, email, password):
#       if not username or not email or not password:
#           raise ValueError("Field is empty")
#       user = self.model(
#                   username = username,
#                   email = email
#                   )
#       user.set_password(password)
#       user.save(using=self._db)
#       return user
#   def create_superuser(self, username, email, password):
#       if not username or not email or not password:
#           raise ValueError("Field is empty")
#       user = self.model(
#                   username = username,
#                   email = email
#                   )
#       user.set_password(password)
#       user.save(using=self._db)
#       return user


#class User(AbstractBaseUser):
#   username = models.CharField(max_length=15, unique=True)
#   email = models.EmailField(max_length=40, verbose_name="email address")
#   objects = UserManager()

#   # Must defined objects
#   is_active = models.BooleanField(default=True)
#   USERNAME_FIELD = 'username'
#   REQUIRED_FIELD = ['email']
#   def get_full_name(self):
#       return self.username
#   def get_short_name(self):
#       return self.username




