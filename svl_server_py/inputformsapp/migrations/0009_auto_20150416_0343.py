# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0008_auto_20150413_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='wordLanguage',
            field=models.ForeignKey(default=1, to='inputformsapp.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='wordType',
            field=models.ForeignKey(default=1, to='inputformsapp.Type'),
            preserve_default=False,
        ),
    ]
