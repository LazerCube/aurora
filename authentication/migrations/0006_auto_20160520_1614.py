# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-20 15:14
from __future__ import unicode_literals

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20160520_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='/static/images/defaults/default-avatar.png', upload_to=authentication.models.get_image_path),
        ),
    ]
