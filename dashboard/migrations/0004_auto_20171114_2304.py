# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_motime_logs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='motime_logs',
            new_name='MotimeLogs',
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='emp_shift_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
