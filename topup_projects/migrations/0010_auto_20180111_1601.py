# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-11 10:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topup_projects', '0009_auto_20180107_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='topup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=100)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 11, 16, 1, 49, 702000))),
                ('status', models.SmallIntegerField(choices=[(0, 'Processing'), (1, 'Success'), (2, 'Failed')])),
                ('amount', models.ManyToManyField(blank=True, to='topup_projects.Product')),
                ('type', models.ManyToManyField(blank=True, to='topup_projects.Operator')),
            ],
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]