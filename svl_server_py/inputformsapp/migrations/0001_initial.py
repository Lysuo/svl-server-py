# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameChapter', models.CharField(max_length=100)),
                ('mDl', models.BooleanField(default=False)),
                ('mFile', models.FileField(upload_to=b'chapters/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameLanguage', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameType', models.CharField(max_length=100)),
                ('typeLanguage', models.ForeignKey(to='inputformsapp.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('french', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('wordChapter', models.ForeignKey(to='inputformsapp.Type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chapter',
            name='chapterLanguage',
            field=models.ForeignKey(to='inputformsapp.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chapter',
            name='chapterType',
            field=models.ForeignKey(to='inputformsapp.Type'),
            preserve_default=True,
        ),
    ]
