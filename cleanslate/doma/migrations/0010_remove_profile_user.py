# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 23:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doma', '0009_auto_20171127_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
