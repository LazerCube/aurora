# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='source',
            new_name='video',
        ),
    ]
