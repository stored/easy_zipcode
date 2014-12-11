# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zipcode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zipcode',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='logradouro', blank=True),
        ),
    ]
