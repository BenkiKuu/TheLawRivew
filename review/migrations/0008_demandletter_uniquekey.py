# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-05 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_auto_20180905_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandletter',
            name='uniquekey',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
