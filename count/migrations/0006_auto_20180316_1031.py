# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-16 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0005_auto_20180316_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastored',
            name='action_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='datastored',
            name='count_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='count.Count'),
            preserve_default=False,
        ),
    ]