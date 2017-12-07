from django.db import models


# Create your models here.
class EmployeeOvertime(models.Model):
    ot_id = models.AutoField(primary_key=True)
    ot_date = models.DateField(blank=True, null=True)
    ot_hrs = models.IntegerField(blank=True, null=True)
    ot_type = models.CharField(max_length=20, blank=True, null=True)
    ot_date_request = models.DateField(blank=True, null=True)
    ot_approved = models.IntegerField(blank=True, null=True, default=0)
    ot_approved_desc = models.CharField(max_length=50, blank=True, null=True)
    emp_id = models.ForeignKey('dashboard.EmployeeDetail', on_delete=None)
    approve_by = models.CharField(max_length=30, blank=True, null=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.ot_date) + " " + str(self.ot_hrs) + " " + self.ot_type + " " + str(self.emp_id)
