# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-14 01:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181214_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='phone',
        ),
    ]
