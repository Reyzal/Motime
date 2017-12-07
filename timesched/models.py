from django.db import models


# Create your models here.
class EmployeeTimeSched(models.Model):
    ts_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('dashboard.EmployeeDetail', on_delete=None)
    ts_timein_date = models.DateField(blank=True, null=True)
    ts_aprove = models.IntegerField(blank=True, null=True, default=0)
    ts_approve_desc = models.CharField(max_length=50, blank=True, null=True)
    approve_by = models.CharField(max_length=30, blank=True, null=True)
    ts_approve_date = models.DateField(blank=True, null=True)
    ts_shift_code = models.ForeignKey('dashboard.EmployeeSchedule', on_delete=None)
    ts_remarks = models.CharField(max_length=250, blank=True, null=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_id) + ' ' + str(self.ts_timein_date)