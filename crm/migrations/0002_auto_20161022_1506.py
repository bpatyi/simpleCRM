# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboundcontact',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
