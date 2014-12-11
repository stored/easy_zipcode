# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zipcode', '0003_state_uf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zipcode',
            name='unit',
        ),
    ]
