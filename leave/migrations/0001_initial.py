# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLeave',
            fields=[
                ('lv_id', models.AutoField(primary_key=True, serialize=False)),
                ('lv_type', models.CharField(blank=True, max_length=30, null=True)),
                ('lv_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('lv_date_start', models.DateField(blank=True, null=True)),
                ('lv_date_end', models.DateField(blank=True, null=True)),
                ('lv_date_request', models.DateField(blank=True, null=True)),
                ('lv_approve', models.IntegerField(blank=True, default=0, null=True)),
                ('lv_approve_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('lv_shift', models.CharField(blank=True, max_length=50, null=True)),
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