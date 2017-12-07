from django.db import models


# Create your models here.
class EmployeeLeave(models.Model):
    lv_id = models.AutoField(primary_key=True)
    lv_type = models.CharField(max_length=30, blank=True, null=True)
    lv_desc = models.CharField(max_length=50, blank=True, null=True)
    lv_date_start = models.DateField(blank=True, null=True)
    lv_date_end = models.DateField(blank=True, null=True)
    lv_date_request = models.DateField(blank=True, null=True)
    lv_approve = models.IntegerField(blank=True, null=True, default=0)
    lv_approve_desc = models.CharField(max_length=50, blank=True, null=True)
    lv_shift = models.CharField(max_length=50, blank=True, null=True)
    emp_id = models.ForeignKey('dashboard.EmployeeDetail', on_delete=None)
    approve_by = models.CharField(max_length=30, blank=True, null=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_id) + "  " + self.lv_type + "  " + self.lv_desc
