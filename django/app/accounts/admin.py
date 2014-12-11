# -*- coding: utf-8 -*-
from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'token')
    list_display_links = ('name', 'email', )
    search_fields = ['name', 'email', 'url', 'token']

admin.site.register(Account, AccountAdmin)