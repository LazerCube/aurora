# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 13:15
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0002_auto_20160517_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
