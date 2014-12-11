# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('token', models.CharField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, max_length=64, verbose_name='token')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
