# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0005_auto_20150412_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='mDateLastUpdate',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 0, 4, 48, 578571, tzinfo=utc), auto_now=True, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chapter',
            name='mLastUpdate',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
