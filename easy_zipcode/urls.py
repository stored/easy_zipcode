# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from views import zipcode_view


urlpatterns = patterns(
    '',
    url(r'$', zipcode_view),
)
