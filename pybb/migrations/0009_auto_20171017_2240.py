# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-17 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0008_auto_20170831_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='autosubscribe',
            field=models.BooleanField(default=True, help_text='Automatically subscribe to topics that you answer', verbose_name='Automatically subscribe'),
        ),
    ]
