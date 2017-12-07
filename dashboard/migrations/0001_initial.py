# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAdpReport',
            fields=[
                ('adp_id', models.AutoField(primary_key=True, serialize=False)),
                ('l_wop', models.IntegerField(blank=True, null=True)),
                ('tardy', models.IntegerField(blank=True, null=True)),
                ('under_time', models.IntegerField(blank=True, null=True)),
                ('overtime', models.IntegerField(blank=True, null=True)),
                ('night_dif', models.IntegerField(blank=True, null=True)),
                ('legal_holiday', models.IntegerField(blank=True, null=True)),
                ('legal_holiday_nd', models.IntegerField(blank=True, null=True)),
                ('legal_holiday_ot', models.IntegerField(blank=True, null=True)),
                ('legal_holiday_rdnd', models.IntegerField(blank=True, null=True)),
                ('legal_holiday_rdot', models.IntegerField(blank=True, null=True)),
                ('special_holiday', models.IntegerField(blank=True, null=True)),
                ('special_holiday_nd', models.IntegerField(blank=True, null=True)),
                ('special_holiday_ot', models.IntegerField(blank=True, null=True)),
                ('special_holiday_rdnd', models.IntegerField(blank=True, null=True)),
                ('special_holiday_rdot', models.IntegerField(blank=True, null=True)),
                ('pay_cycle_from', models.DateField(blank=True, null=True)),
                ('pay_cycle_to', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('change_by', models.CharField(blank=True, max_length=30, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default='01')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDepartment',
            fields=[
                ('emp_department_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('department_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('change_by', models.CharField(blank=True, max_length=30, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default='01')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_shift_code', models.CharField(blank=True, max_length=20, null=True)),
                ('emp_firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_middlename', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('emp_birthdate', models.DateTimeField(blank=True, null=True)),
                ('emp_gender', models.CharField(blank=True, max_length=1, null=True)),
                ('emp_status', models.IntegerField(blank=True, null=True)),
                ('emp_date_hired', models.DateTimeField(blank=True, null=True)),
                ('emp_history', models.CharField(blank=True, max_length=12, null=True)),
                ('emp_wave_no', models.CharField(blank=True, max_length=12, null=True)),
                ('emp_team', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_leave_credit', models.IntegerField(blank=True, null=True)),
                ('profile_pic', models.FileField(blank=True, default='1.jpeg', upload_to='')),
                ('created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('change_by', models.CharField(blank=True, max_length=30, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default='01')),
                ('emp_department_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EmployeeDepartment')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('emp_position_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('position_desc', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('change_by', models.CharField(blank=True, max_length=30, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default='01')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSchedule',
            fields=[
                ('emp_shift_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_shift_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_schedule_time', models.TimeField(blank=True, null=True)),
                ('start_schedule_date', models.DateField(blank=True, null=True)),
                ('end_schedule_end', models.TimeField(blank=True, null=True)),
                ('end_schedule_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('change_by', models.CharField(blank=True, max_length=30, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default='01')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EmployeeDetail')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTracker',
            fields=[
                ('time_tracker_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_in_date', models.DateField(blank=True, null=True)),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('time_in_lunch', models.TimeField(blank=True, null=True)),
                ('time_out_lunch', models.TimeField(blank=True, null=True)),
                ('time_in_break', models.TimeField(blank=True, null=True)),
                ('time_out_break', models.TimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('change_by', models.CharField(blank=True, max_length=30, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('action_flag', models.CharField(blank=True, max_length=5, null=True)),
                ('status', models.IntegerField(default='01')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EmployeeDetail')),
                ('emp_shift_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EmployeeSchedule')),
            ],
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='emp_position_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EmployeePosition'),
        ),
        migrations.AddField(
            model_name='employeeadpreport',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.EmployeeDetail'),
        ),
    ]