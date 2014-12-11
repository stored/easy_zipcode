# -*- coding: utf-8 -*-
import logging, json, requests

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.resources import skip_prepare

from accounts.models import Account
from zipcode.models import ZipCode
from zipcode.tasks import create_zipcode

logger = logging.getLogger('zipcode.resources')


class ZipCodeResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'zip_code': 'zip_code',
        'city': 'city.name',
        'address': 'address',
        'complement': 'complement',
        'area': 'area',
        'ibge': 'city.ibge'
    })

    def is_authenticated(self):
        try:
            Account.objects.get(token=self.request.GET.get('token'))
            logger.info("Authenticate Success")
            return True
        except Account.DoesNotExist:
            logger.error("Account does not exist")
            return False

    def get_zipcode_info(self, zip_code):
        try:
            zipcode_info = requests.get('http://api.postmon.com.br/v1/cep/'+str(zip_code)).content
            logger.info("Zipcode info Success")
            return json.loads(zipcode_info)
        except:
            logger.info("Zipcode does not exist")
            pass
        
    @skip_prepare
    def prepare_postmon(self, postmon_data):
        brzipcode_data = {
            'zip_code': postmon_data.get('cep', ''),
            'city': postmon_data.get('cidade', ''),
            'address': postmon_data.get('logradouro', ''),
            'complement': postmon_data.get('complemento', ''),
            'area': postmon_data.get('bairro', ''),
            'ibge': postmon_data.get('cidade_info: {codigo_ibge}', ''),
        }
        logger.info("Prepare Success")
        return brzipcode_data

    def list(self):
        logger.info("List zipcodes Success")
        return ZipCode.objects.all()

    def detail(self, pk):
        try:
            logger.info("Detail zipcode Success")
            return ZipCode.objects.get(zip_code=pk)
        except:
            postmon_data = self.get_zipcode_info(pk)
            create_zipcode.delay(postmon_data)
            logger.info("Return and create zipcode Success")
            return self.prepare_postmon(postmon_data)