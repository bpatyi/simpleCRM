# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20161009_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboundcontact',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inboundcontact',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
