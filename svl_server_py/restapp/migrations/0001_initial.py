# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 18:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inputformsapp', '0010_auto_20160117_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfosChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mTitle', models.CharField(default=b'false', max_length=50)),
                ('isInProgress', models.CharField(default=b'false', max_length=20)),
                ('mLastUpdated', models.CharField(default=b'false', max_length=50)),
                ('mIdC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputformsapp.Chapter')),
                ('mUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InfosWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mTitle', models.CharField(default=b'false', max_length=50)),
                ('mFailed', models.IntegerField()),
                ('mSeen', models.IntegerField()),
                ('isBookmarked', models.CharField(default=b'false', max_length=20)),
                ('mLastRevisionTS', models.CharField(default=b'false', max_length=50)),
                ('mPropStat', models.FloatField()),
                ('mIdC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputformsapp.Chapter')),
                ('mIdW', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputformsapp.Word')),
                ('mUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
