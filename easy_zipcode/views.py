# coding: utf-8
import json

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

from main import EasyZipCode


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content,
                             content_type='application/json',
                             **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)


class EasyZipCodeView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        zip_code = request.GET.get('zip_code').replace("-", "")
        token = settings.EASY_ZIPCODE_TOKEN
        return HttpResponse(EasyZipCode.get_zipcode(zip_code, token, plain_text=True), content_type="application/json")
