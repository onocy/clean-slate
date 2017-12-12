# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('doma', '0024_auto_20171212_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bedtime',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pet_allergies',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='smokes',
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Online', 'online'), ('Offline', 'offline'), ('Busy', 'busy'), ('On Vacation', 'vacation')], default='online', help_text='Select a status for others to view', max_length=8),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
