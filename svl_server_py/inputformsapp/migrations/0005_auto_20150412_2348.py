# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0004_auto_20150410_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='mProp',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='mSeen',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='mSuccess',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
