# -*- coding: utf-8 -*-
from django.contrib import admin

from zipcode.models import State, City, ZipCode


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'ibge', 'area_km2')
    list_display_links = ('name',)
    search_fields = ['name', 'ibge']


class CityAdmin(admin.ModelAdmin):
    list_display = ('state', 'name', 'ibge', 'area_km2')
    list_display_links = ('name',)
    search_fields = ['name', 'ibge']


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ('city', 'zip_code', 'address', 'complement', 'area')
    list_display_links = ('zip_code', 'address', 'complement', 'area')
    search_fields = ['zip_code', 'address', 'complement',]


admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(ZipCode, ZipCodeAdmin)    