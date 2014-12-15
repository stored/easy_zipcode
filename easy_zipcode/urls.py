# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import EasyZipCodeDetailView


urlpatterns = patterns(
    '',
    url(r'$', EasyZipCodeDetailView.as_view()),
)
