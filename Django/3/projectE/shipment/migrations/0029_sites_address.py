# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0028_auto_20160717_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='address',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]