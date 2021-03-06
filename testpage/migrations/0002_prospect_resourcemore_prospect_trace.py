# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-07-29 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect_resourcemore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.CharField(max_length=20)),
                ('NAME', models.CharField(max_length=100)),
                ('RESOURCE', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testpage.Prospect_resource')),
            ],
            options={
                'db_table': 'PROSPECT_RESOURCEMORE',
            },
        ),
        migrations.CreateModel(
            name='Prospect_trace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.CharField(max_length=20)),
                ('NAME', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'PROSPECT_TRACE',
            },
        ),
    ]
