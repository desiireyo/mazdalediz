# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-08-14 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0004_custmast_officer_prospect_test_setcolor_setmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='INVTRAN',
            fields=[
                ('RECVNO', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('RECVDT', models.DateField(blank=True, null=True)),
                ('GCODE', models.CharField(blank=True, max_length=3, null=True)),
                ('TYPE', models.CharField(blank=True, max_length=12, null=True)),
                ('BAAB', models.CharField(blank=True, max_length=20, null=True)),
                ('COLOR', models.CharField(blank=True, max_length=12, null=True)),
                ('STRNO', models.CharField(blank=True, max_length=20, null=True)),
                ('ENGNO', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'INVTRAN',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SECRET',
            fields=[
                ('USERID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('ENDCODE', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'SECRET',
                'managed': False,
            },
        ),
    ]
