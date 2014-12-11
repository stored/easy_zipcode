# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns(
    '',
    url(r'$', views.zipcode_info, name='easy_zipcode'),
)
