# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topup_projects', '0006_dtgfsghr'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtgfsghr',
            name='sifat_fls',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reload_countryToDG', to='topup_projects.Reload_country'),
        ),
    ]