# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-30 15:10
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='avatar/default.png', upload_to='avatar/%Y/%m/%d', verbose_name='头像'),
        ),
    ]