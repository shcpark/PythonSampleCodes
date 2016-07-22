# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-16 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0019_auto_20160716_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='loadage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customers',
            name='address',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='chief',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='fax',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='manager',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='standard',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='standard',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='규격',
            name='단가',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='규격',
            name='운반비',
            field=models.IntegerField(default=0),
        ),
    ]