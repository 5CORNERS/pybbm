# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-17 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0012_like_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='receive_emails',
            field=models.BooleanField(default=True),
        ),
    ]
