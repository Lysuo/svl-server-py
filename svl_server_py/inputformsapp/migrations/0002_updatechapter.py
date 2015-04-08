# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputformsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateChapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mFileUpdate', models.FileField(upload_to=b'chapters/')),
                ('chapterLanguageUpdate', models.ForeignKey(to='inputformsapp.Language')),
                ('chapterTypeUpdate', models.ForeignKey(to='inputformsapp.Type')),
                ('nameChapterUpdate', models.ForeignKey(to='inputformsapp.Chapter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
