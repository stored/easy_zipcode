# coding: utf-8
import json

from django.conf import settings
from django.http import HttpResponse

from main import EasyZipCode


def zipcode_view(request):
    return HttpResponse(json.dumps(EasyZipCode.get_zipcode(
        zip_code=request.GET.get('zip_code'),
        token=settings.EASY_ZIPCODE_TOKEN,
        plain_text=True,
    )), content_type="application/json")
