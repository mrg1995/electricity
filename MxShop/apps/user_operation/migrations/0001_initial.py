# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-17 00:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(default='', help_text='售后区域', max_length=50, verbose_name='售后区域')),
                ('address', models.CharField(default='', help_text='详细地址', max_length=200, verbose_name='详细地址')),
                ('signer_name', models.CharField(default='', help_text='签收人姓名', max_length=100, verbose_name='签收人姓名')),
                ('signer_mobile', models.CharField(default='', help_text='收货人电话', max_length=11, verbose_name='收货人电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户售后地址管理',
                'verbose_name_plural': '用户售后地址管理',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='收藏时间', verbose_name='收藏时间')),
                ('goods', models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserLeavingMesage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_type', models.IntegerField(choices=[(0, '留言'), (1, '投诉'), (2, '询问'), (3, '售后'), (4, '求购')], help_text='留言类型', verbose_name='留言类型')),
                ('message', models.CharField(default='', help_text='留言内容', max_length=100, verbose_name='留言内容')),
                ('file', models.FileField(help_text='上传文件', max_length=200, upload_to='UserLeavingMesage/%Y/%m', verbose_name='上传文件')),
                ('subject', models.CharField(default='', help_text='留言标题', max_length=100, verbose_name='留言标题')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户留言管理',
                'verbose_name_plural': '用户留言管理',
            },
        ),
    ]
