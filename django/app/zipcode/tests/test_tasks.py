# -*- coding: utf-8 -*-
from django.test import TestCase

from accounts.tests.factories import AccountFactory
from zipcode.tasks import create_zipcode, import_zipcode
from zipcode.models import ZipCode


class CreateZipCode(TestCase):
    def setUp(self):
        self.add_account = AccountFactory.create()

    def test_01_create_zipcode(self):
        create_zipcode(
            {
                'city': 'Ribeirão Preto',
                'ibge': '3543402',
                'area': 'Alto da Boa Vista',
                'complement': '',
                'address': 'Avenida Presidente Vargas',
                'zip_code': '14020260'
            }
        )
        self.assertEqual(ZipCode.objects.all().count(), 1)

    def test_02_import_zipcode(self):
        import_zipcode(14110000, 14110001)

    def test_03_invalid_zipcode(self):
        import_zipcode(00000000, 00000001)