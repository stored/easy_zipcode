# -*- coding: utf-8 -*-
import logging, json, requests
from celery import Celery, task

from zipcode.models import ZipCode, State, City

app = Celery('tasks', broker='redis://localhost:6379/0')

logger = logging.getLogger('zipcode.tasks')


@task
def create_zipcode(info):
    state, created = State.objects.get_or_create(
        name = info.get('estado_info', {}).get('nome', ''),
        ibge = info.get('estado_info', {}).get('codigo_ibge', ''),
        area_km2 = info.get('estado_info', {}).get('area_km2', ''),
        uf = info.get('estado', ''),
    )
    logger.info("Create state Success")
    
    city, created = City.objects.get_or_create(
        state = state,
        name = info.get('cidade', ''),
        ibge = info.get('cidade_info', {}).get('codigo_ibge', ''),
        area_km2 = info.get('cidade_info', {}).get('area_km2', ''),
    )
    logger.info("Create city Success")
    
    create_zipcode, created = ZipCode.objects.get_or_create(
        zip_code = info.get('cep', ''),
        city = city,
        address = info.get('logradouro', ''),
        complement = info.get('complemento', ''),
        area = info.get('bairro', ''),
    )
    logger.info("Create zipcode Success")

@task
def import_zipcode(start_zipcode=10000000, end_zip_code=99999999):
    for zipcode in range(start_zipcode, end_zip_code):
        try:
            print zipcode
            zipcode_info = requests.get('http://api.postmon.com.br/v1/cep/'+str(zipcode)).content
            zip_code_json = json.loads(zipcode_info)
            create_zipcode.delay(zip_code_json)
            logger.info("Import Zipcode Success")
        except:
            logger.info("Zipcode does not exist")
            pass