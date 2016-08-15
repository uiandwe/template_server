__author__ = 'uiandwe'

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^(?P<template_name>\w+)/$', 'view_templates.views.show_templates'),
                       )

