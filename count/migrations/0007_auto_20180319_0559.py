# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-19 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0006_auto_20180316_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datastored',
            old_name='count_id',
            new_name='count',
        ),
    ]