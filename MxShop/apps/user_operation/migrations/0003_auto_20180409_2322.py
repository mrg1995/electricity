# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20180408_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default='', help_text='城市', max_length=100, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='province',
            field=models.CharField(default='', help_text='省份', max_length=100, verbose_name='省份'),
        ),
    ]
