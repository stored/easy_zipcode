# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zipcode', '0004_remove_zipcode_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area_km2',
            field=models.CharField(max_length=100, null=True, verbose_name='area km2', blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='area_km2',
            field=models.CharField(max_length=100, null=True, verbose_name='area km2', blank=True),
        ),
    ]
