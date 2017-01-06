from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions
from account.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
#   class Meta:
#       model = User
#       fields = ('username', 'email','password')

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=20)
#   class Meta:
#       model = User
#       fields = ('password')

class UserSearchSerializer(serializers.BaseSerializer):
    name = serializers.CharField()
    def to_representation(self, obj):
        return {'name', obj.name}
