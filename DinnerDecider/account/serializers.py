from django.contrib.auth.models import User, Group
from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

