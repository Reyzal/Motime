# Generated by Django 2.0 on 2017-12-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overtime', '0002_employeeovertime_ot_approved_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeovertime',
            name='emp_id',
            field=models.ForeignKey(on_delete=None, to='dashboard.EmployeeDetail'),
        ),
    ]
