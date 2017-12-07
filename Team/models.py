from django.db import models


class EmployeeTeam(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_desc = models.CharField(max_length=50, null=True, blank=True)
    emp_id = models.ForeignKey('dashboard.EmployeeDetail', on_delete=None)
    emp_position_ID = models.IntegerField(null=True, blank=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.team_id) + ' ' + self.team_desc


class EmployeeTeamMembers(models.Model):
    member_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('EmployeeTeam', on_delete=models.CASCADE)
    emp_id = models.ForeignKey('dashboard.EmployeeDetail', on_delete=None)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.team_id) + ' ' + str(self.emp_id)
