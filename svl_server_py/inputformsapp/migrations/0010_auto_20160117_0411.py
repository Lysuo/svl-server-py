# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0009_auto_20150416_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='mDLU',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]