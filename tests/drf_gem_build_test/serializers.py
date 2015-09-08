# coding: utf-8
from rest_framework import serializers
import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)

    def update(self, attrs, instance=None):
        user = super(UserSerializer, self).update(attrs, instance)
        user.set_password(attrs['password'])
        return user


