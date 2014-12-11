# -*- coding: utf-8 -*-
from django.db import models


class State(models.Model):
    name = models.CharField(u'nome', max_length=255)
    ibge = models.CharField(u'ibge', max_length=2, null=True, blank=True)
    uf = models.CharField(u'sigla', max_length=2)
    area_km2 = models.CharField(u'area km2', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'{}'.format(self.name)


class City(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(u'nome', max_length=255)
    ibge = models.CharField(u'ibge', max_length=7, null=True, blank=True)
    area_km2 = models.CharField(u'area km2', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'{}'.format(self.name)


class ZipCode(models.Model):
    zip_code = models.CharField(u'cep', max_length=8)
    city = models.ForeignKey(City)
    address = models.CharField(u'logradouro', max_length=255, null=True, blank=True)
    complement = models.CharField(u'complemento', max_length=255, null=True, blank=True)
    area = models.CharField(u'bairro', max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u'{}'.format(self.zip_code)
