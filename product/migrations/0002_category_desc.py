# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=500, verbose_name='分类描述'),
        ),
    ]