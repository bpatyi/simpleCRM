# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 13:20
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20161102_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutboundContactEmailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_unsubscribed', models.BooleanField(default=False)),
                ('is_soft_bounced', models.BooleanField(default=False)),
                ('is_hard_bounced', models.BooleanField(default=False)),
                ('open_times', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), blank=True, size=None)),
                ('clicked_links', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=255), blank=True, size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutboundContactMailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_deliverable', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutboundContactPhoneInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('call_times', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), blank=True, size=None)),
                ('success_call_times', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), blank=True, size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='inboundcontact',
            name='searchable_channels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('M', 'Mail'), ('E', 'Email'), ('P', 'Phone')], max_length=1), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='outboundcontact',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Campaign'),
        ),
        migrations.AddField(
            model_name='outboundcontact',
            name='contact_type',
            field=models.CharField(choices=[('M', 'Mail'), ('E', 'Email'), ('P', 'Phone')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='outboundcontact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outboundcontact',
            name='date_of_contact',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='outboundcontact',
            name='is_success',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='outboundcontact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='inboundcontactaddress',
            name='inbound_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='crm.InboundContact'),
        ),
        migrations.AlterField(
            model_name='inboundcontactemail',
            name='inbound_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='crm.InboundContact'),
        ),
        migrations.AlterField(
            model_name='inboundcontactphone',
            name='inbound_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='crm.InboundContact'),
        ),
        migrations.AlterField(
            model_name='individualaddress',
            name='individual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='crm.Individual'),
        ),
        migrations.AlterField(
            model_name='individualemail',
            name='individual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='crm.Individual'),
        ),
        migrations.AlterField(
            model_name='individualphone',
            name='individual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='crm.Individual'),
        ),
        migrations.AddField(
            model_name='outboundcontactphoneinfo',
            name='outbound_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_infos', to='crm.OutboundContact'),
        ),
        migrations.AddField(
            model_name='outboundcontactphoneinfo',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.IndividualPhone'),
        ),
        migrations.AddField(
            model_name='outboundcontactmailinfo',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.IndividualAddress'),
        ),
        migrations.AddField(
            model_name='outboundcontactmailinfo',
            name='outbound_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail_info', to='crm.OutboundContact'),
        ),
        migrations.AddField(
            model_name='outboundcontactemailinfo',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.IndividualEmail'),
        ),
        migrations.AddField(
            model_name='outboundcontactemailinfo',
            name='outbound_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_infos', to='crm.OutboundContact'),
        ),
    ]
