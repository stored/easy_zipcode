# -*- coding: utf-8 -*-
import json, requests

from django.test import TestCase

from accounts.tests.factories import AccountFactory


class ZipCodeTest(TestCase):
    def setUp(self):
        self.add_account = AccountFactory.create()

    def test_01_authentication(self):
        response = self.client.get('/api/?token={0}'.format(self.add_account.token))

    def test_02_not_authentication(self):
        response = self.client.get('/api/?token=sadhjas')
        
    def test_03_zipcode_detail(self):
        get_zipcode_info = self.client.get('/api/14020260/?token={0}'.format(self.add_account.token))

    def test_04_zipcode_does_not_exist(self):
        get_zipcode_info = self.client.get('/api/10000000/?token={0}'.format(self.add_account.token))
