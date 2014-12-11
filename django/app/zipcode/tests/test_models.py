# -*- coding: utf-8 -*-
from django.test import TestCase

from factories import StateFactory, \
    CityFactory, ZipCodeFactory


class StateTest(TestCase):
    def setUp(self):
        self.add_state = StateFactory.create()

    def test_unicode(self):
        self.assertEqual(u'São Paulo', unicode(self.add_state))


class CityTest(TestCase):
    def setUp(self):
        self.add_city = CityFactory.create()

    def test_unicode(self):
        self.assertEqual(u'Ribeirão Preto', unicode(self.add_city))


class ZipCodeTest(TestCase):
    def setUp(self):
        self.add_zipcode = ZipCodeFactory.create()

    def test_unicode(self):
        self.assertEqual(u'14025700', unicode(self.add_zipcode))