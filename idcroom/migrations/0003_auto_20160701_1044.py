# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idcroom', '0002_auto_20160606_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcroom',
            name='name',
            field=models.CharField(default='', max_length=256, verbose_name='\u673a\u623f\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='idcroom',
            name='user',
            field=models.CharField(default='', max_length=256, verbose_name='\u64cd\u4f5c\u5458'),
        ),
    ]