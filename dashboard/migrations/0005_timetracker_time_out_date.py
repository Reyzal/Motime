# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20171114_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetracker',
            name='time_out_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]