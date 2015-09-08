# coding: utf-8
from rest_framework.filters import DjangoFilterBackend
from rest_framework import viewsets
from django.contrib.auth.models import User
import models
import serializers


class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['username', 'email']

