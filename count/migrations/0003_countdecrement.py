# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-15 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0002_auto_20180315_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountDecrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decrement', models.IntegerField()),
            ],
        ),
    ]
