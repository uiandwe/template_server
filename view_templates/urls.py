__author__ = 'uiandwe'

from django.conf.urls import include, url

from . import views

urlpatterns = [url(r'^(?P<template_name>\w+)/$', views.show_templates), ]

