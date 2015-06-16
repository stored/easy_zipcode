# -*- coding: utf-8 -*-
try:
	from django.conf.urls import patterns, include, url
except:
	from django.conf.urls.defaults import patterns, include, url

from views import EasyZipCodeView


urlpatterns = patterns(
    '',
    url(r'$', EasyZipCodeView.as_view(), name='easy_zipcode'),
)
