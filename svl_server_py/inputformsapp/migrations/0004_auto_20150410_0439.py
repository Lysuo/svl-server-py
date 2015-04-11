# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0003_auto_20150408_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='mFile',
            field=models.FileField(upload_to=b'media/chapters/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='updatechapter',
            name='mFileUpdate',
            field=models.FileField(upload_to=b'media/chapters/'),
            preserve_default=True,
        ),
    ]
