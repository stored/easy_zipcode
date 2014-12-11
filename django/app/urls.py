# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from zipcode.resources import ZipCodeResource


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(ZipCodeResource.urls())),
)
