# -*- coding: utf-8 -*-
import json
import requests

URL = 'http://easyzipcode.com/api/v1/%(zip_code)s/?token=%(token)s'


class EasyZipCode(object):
    @classmethod
    def get_zipcode_info(cls, zip_code, token, plain_text=False):
        req = requests.get(URL % {
            'zip_code': zip_code,
            'token': token,
        })

        if plain_text:
            return req.content
        return json.loads(req.content)
