# -*- coding: utf-8 -*-
import uuid

from django.db import models


class Account(models.Model):
    token = models.CharField(u'token', max_length=64, primary_key=True, 
        editable=False, default=uuid.uuid4)
    name = models.CharField(u'nome', max_length=255)
    email = models.CharField(u'email', max_length=255)
    url = models.CharField(u'url', max_length=255)

    def __unicode__(self):
        return u'{}'.format(self.token)
