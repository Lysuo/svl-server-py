# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0007_auto_20150413_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='mDl',
            field=models.CharField(default=b'false', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='mLU',
            field=models.CharField(default=b'true', max_length=20),
            preserve_default=True,
        ),
    ]
