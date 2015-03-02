# -*- coding: utf-8 -*-
try:
	from django.conf.urls import patterns, include, url
except:
	from django.conf.urls.defaults import patterns, include, url

from views import zipcode_view


urlpatterns = patterns(
    '',
    url(r'$', zipcode_view),
)
