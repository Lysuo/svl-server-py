# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoschapter',
            old_name='mLastUpdated',
            new_name='mLastCompleted',
        ),
    ]
