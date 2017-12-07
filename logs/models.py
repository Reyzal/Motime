from django.db import models


# holds logs on all events in motime
class EmployeeLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('dashboard.EmployeeDetail', on_delete=None)
    log_action = models.CharField(max_length=255, blank=True)
    log_date = models.DateField(blank=True, null=True)
    log_time = models.TimeField(blank=True, null=True)
    log_out = models.TimeField(blank=True, null=True)

    overtime = models.IntegerField(blank=True, null=True)
    total_late = models.IntegerField(blank=True, null=True)
    night_def = models.IntegerField(blank=True, null=True)
    lwop = models.IntegerField(blank=True, null=True)
    undertime = models.IntegerField(blank=True, null=True)

    start_break = models.TimeField(blank=True, null=True)
    end_break = models.TimeField(blank=True, null=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.log_id) + "  " + str(self.log_date) + "  " + self.log_action
