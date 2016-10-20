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


class ProjetoView(viewsets.ModelViewSet):
    serializer_class = serializers.ProjetoSerializer
    queryset = models.Projeto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['nome', 'repositorio']


class TagsView(viewsets.ModelViewSet):
    serializer_class = serializers.TagsSerializer
    queryset = models.Tags.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['nome', 'tipo']


class StatusHttpView(viewsets.ModelViewSet):
    serializer_class = serializers.StatusHttpSerializer
    queryset = models.StatusHttp.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['codigo', 'tipo', 'descricao']


class EndpointView(viewsets.ModelViewSet):
    serializer_class = serializers.EndpointSerializer
    queryset = models.Endpoint.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['path', 'metodo', 'saida', 'descricao', 'solicitante', 'executor', 'created', 'status', 'projeto', 'tag', 'status_http_erro', 'mensagem_erro', 'mensagem_sucesso', 'status_http_sucesso']


class EntradaView(viewsets.ModelViewSet):
    serializer_class = serializers.EntradaSerializer
    queryset = models.Entrada.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['chave', 'valor', 'endpoint']


class ComentarioView(viewsets.ModelViewSet):
    serializer_class = serializers.ComentarioSerializer
    queryset = models.Comentario.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['comentario', 'like', 'created', 'usuario', 'endpoint']
