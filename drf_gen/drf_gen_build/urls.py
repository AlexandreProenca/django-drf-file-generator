# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'list')
router.register(r'projetos', views.ProjetoView, 'list')
router.register(r'tagss', views.TagsView, 'list')
router.register(r'statushttps', views.StatusHttpView, 'list')
router.register(r'endpoints', views.EndpointView, 'list')
router.register(r'entradas', views.EntradaView, 'list')
router.register(r'comentarios', views.ComentarioView, 'list')

urlpatterns = patterns('',)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('', url(r'^', include(router.urls)),)
