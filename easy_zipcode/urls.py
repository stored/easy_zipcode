# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import EasyZipCodeView


urlpatterns = [
    url(r'$', EasyZipCodeView.as_view(), name='easy_zipcode'),
]
