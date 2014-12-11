# -*- coding: utf-8 -*-
from django.test import TestCase

from factories import AccountFactory


class AccountTest(TestCase):
    def setUp(self):
        self.add_account = AccountFactory.create()

    def test_unicode(self):
        self.assertEqual(u'{}'.format(self.add_account), unicode(self.add_account))
