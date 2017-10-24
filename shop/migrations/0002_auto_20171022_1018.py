# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='幻灯片标题')),
                ('order_value', models.IntegerField(default=0, verbose_name='排序值')),
                ('image', models.ImageField(upload_to='adv/%Y/%m', verbose_name='幻灯片图片')),
                ('link', models.CharField(max_length=1000, verbose_name='幻灯片链接')),
                ('status', models.IntegerField(choices=[(0, '隐藏'), (1, '显示')])),
                ('is_abort', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '幻灯片',
                'verbose_name_plural': '幻灯片',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='公告标题')),
                ('order_value', models.IntegerField(default=0, verbose_name='排序值')),
                ('image', models.ImageField(blank=True, null=True, upload_to='notice/%Y/%m', verbose_name='公告图片')),
                ('link', models.CharField(blank=True, max_length=1000, null=True, verbose_name='公告链接')),
                ('status', models.IntegerField(choices=[(0, '隐藏'), (1, '显示')], verbose_name='状态')),
                ('detail', models.TextField(verbose_name='公告详情')),
                ('is_abort', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
    ]