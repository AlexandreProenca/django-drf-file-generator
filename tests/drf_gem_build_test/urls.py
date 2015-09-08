# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'list')

urlpatterns = patterns('',)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('', url(r'^', include(router.urls)),)
