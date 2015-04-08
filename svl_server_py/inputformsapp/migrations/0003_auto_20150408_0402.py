# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0002_updatechapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='wordChapter',
            field=models.ForeignKey(to='inputformsapp.Chapter'),
            preserve_default=True,
        ),
    ]
