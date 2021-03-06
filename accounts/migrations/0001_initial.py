# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 19:05
from __future__ import unicode_literals

import accounts.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=254, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('last_name', models.CharField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=32)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', accounts.managers.CustomUserManager()),
            ],
        ),
    ]
