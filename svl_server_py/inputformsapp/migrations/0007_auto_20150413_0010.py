# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0006_auto_20150413_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='mDateLastUpdate',
            new_name='mDLU',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='mLastUpdate',
            new_name='mLU',
        ),
    ]
