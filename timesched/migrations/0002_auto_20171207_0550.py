# Generated by Django 2.0 on 2017-12-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesched', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetimesched',
            name='emp_id',
            field=models.ForeignKey(on_delete=None, to='dashboard.EmployeeDetail'),
        ),
        migrations.AlterField(
            model_name='employeetimesched',
            name='ts_shift_code',
            field=models.ForeignKey(on_delete=None, to='dashboard.EmployeeSchedule'),
        ),
    ]
