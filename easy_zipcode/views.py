# coding: utf-8
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View

from main import EasyZipCode


class JSONResponseMixin(object):

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        return context


class EasyZipCodeView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        zip_code = request.GET.get('zip_code').replace("-", "")
        token = settings.EASY_ZIPCODE_TOKEN
        data = EasyZipCode.get_zipcode(zip_code, token)
        return self.render_to_response(data)
