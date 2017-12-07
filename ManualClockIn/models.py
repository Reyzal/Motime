from django.db import models


class ManualClockIn(models.Model):
    manual_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('dashboard.EmployeeDetail', on_delete=None)

    manual_date_request = models.DateField(blank=True, null=True)
    start_schedule_time = models.TimeField(blank=True, null=True)
    start_schedule_date = models.DateField(blank=True, null=True)
    end_schedule_time = models.TimeField(blank=True, null=True)
    end_schedule_date = models.DateField(blank=True, null=True)
    manual_remarks = models.CharField(max_length=250, blank=True, null=True)

    manual_approved = models.IntegerField(blank=True, null=True, default=0)
    manual_approved_desc = models.CharField(max_length=50, blank=True, null=True)
    manual_approved_request = models.DateField(blank=True, null=True)
    approve_by = models.CharField(max_length=30, blank=True, null=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_id)
