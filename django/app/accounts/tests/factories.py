# -*- coding: utf-8 -*-
import factory, uuid

from accounts.models import Account


class AccountFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Account

    token = u'3850de3a-2422-482d-92fc-d1a48a71eba1'
    name = u'Fernando'
    email = u'fernando.chimicoviaki@stored.com.br'
    url = 'http://localhost:8000'
