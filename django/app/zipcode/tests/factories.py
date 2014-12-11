# -*- coding: utf-8 -*-
import factory

from zipcode.models import State, City, ZipCode


class StateFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = State

    name = u'São Paulo'
    ibge = u'35'
    uf = u'SP'
    area_km2 = u'248.222,801'


class CityFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = City

    state = factory.SubFactory(StateFactory)
    name = u'Ribeirão Preto'
    ibge = u'3543402'
    area_km2 = u'650,955'


class ZipCodeFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = ZipCode

    zip_code = '14025700'
    city = factory.SubFactory(CityFactory)
    address = u'Avenida Presidente Vargas'
    complement = 'de 1050 a 2698 - lado par'
    area = u'Alto da Boa Vista'