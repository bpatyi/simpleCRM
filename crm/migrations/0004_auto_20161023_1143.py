# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 11:43
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20161023_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='inboundcontactphone',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='individualphone',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]