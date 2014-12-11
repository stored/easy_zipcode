# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('ibge', models.CharField(max_length=7, null=True, verbose_name='ibge', blank=True)),
                ('area_km2', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('ibge', models.CharField(max_length=2, null=True, verbose_name='ibge', blank=True)),
                ('area_km2', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=8, verbose_name='cep')),
                ('address', models.CharField(max_length=255, verbose_name='logradouro')),
                ('complement', models.CharField(max_length=255, null=True, verbose_name='complemento', blank=True)),
                ('area', models.CharField(max_length=255, null=True, verbose_name='bairro', blank=True)),
                ('unit', models.CharField(max_length=255, null=True, verbose_name='unidade', blank=True)),
                ('city', models.ForeignKey(to='zipcode.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='zipcode.State'),
            preserve_default=True,
        ),
    ]
