# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zipcode', '0002_auto_20141126_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='uf',
            field=models.CharField(default=None, max_length=2, verbose_name='sigla'),
            preserve_default=False,
        ),
    ]
