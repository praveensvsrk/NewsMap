# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmap_app', '0004_auto_20170707_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='img',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
