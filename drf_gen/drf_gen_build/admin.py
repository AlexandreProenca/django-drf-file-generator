# coding: utf-8
from django.contrib import admin
import models


class Projeto(admin.ModelAdmin):
    list_display = ['nome', 'repositorio']


class Tags(admin.ModelAdmin):
    list_display = ['nome', 'tipo']


class StatusHttp(admin.ModelAdmin):
    list_display = ['codigo', 'tipo', 'descricao']


class Endpoint(admin.ModelAdmin):
    list_display = ['path', 'metodo', 'saida', 'descricao', 'solicitante', 'executor', 'created', 'status', 'projeto', 'tag', 'status_http_erro', 'mensagem_erro', 'mensagem_sucesso', 'status_http_sucesso']


class Entrada(admin.ModelAdmin):
    list_display = ['chave', 'valor', 'endpoint']


class Comentario(admin.ModelAdmin):
    list_display = ['comentario', 'like', 'created', 'usuario', 'endpoint']

admin.site.register(models.Projeto, Projeto)
admin.site.register(models.Tags, Tags)
admin.site.register(models.StatusHttp, StatusHttp)
admin.site.register(models.Endpoint, Endpoint)
admin.site.register(models.Entrada, Entrada)
admin.site.register(models.Comentario, Comentario)
