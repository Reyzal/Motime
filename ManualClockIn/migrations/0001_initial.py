# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0005_timetracker_time_out_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualClockIn',
            fields=[
                ('manual_id', models.AutoField(primary_key=True, serialize=False)),
                ('manual_date_request', models.DateField(blank=True, null=True)),
                ('start_schedule_time', models.TimeField(blank=True, null=True)),
                ('start_schedule_date', models.DateField(blank=True, null=True)),
                ('end_schedule_time', models.TimeField(blank=True, null=True)),
                ('end_schedule_date', models.DateField(blank=True, null=True)),
                ('manual_remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('manual_approved', models.IntegerField(blank=True, default=0, null=True)),
                ('manual_approved_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('manual_approved_request', models.DateField(blank=True, null=True)),
                ('approve_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('change_by', models.CharField(blank=True, max_length=30, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default='01')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EmployeeDetail')),
            ],
        ),
    ]
