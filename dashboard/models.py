from django.db import models


# model to hold all employee position
class EmployeePosition(models.Model):
    emp_position_ID = models.IntegerField(primary_key=True)
    position_desc = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_position_ID) + "-" + self.position_desc


# model to hold all employee department
class EmployeeDepartment(models.Model):
    emp_department_ID = models.IntegerField(primary_key=True)
    department_desc = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_department_ID) + "-" + self.department_desc


# model to hold all employee details
class EmployeeDetail(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_position_ID = models.ForeignKey('EmployeePosition', on_delete=None)
    emp_department_ID = models.ForeignKey('EmployeeDepartment', on_delete=None)
    emp_shift_code = models.CharField(max_length=20, blank=True, null=True)

    emp_firstname = models.CharField(null=True, blank=True, max_length=30)
    emp_middlename = models.CharField(null=True, blank=True, max_length=30)
    emp_lastname = models.CharField(null=True, blank=True, max_length=30)
    emp_email = models.EmailField(null=True, blank=True)
    emp_birthdate = models.DateTimeField(null=True, blank=True)
    emp_gender = models.CharField(null=True, blank=True, max_length=1)

    emp_status = models.IntegerField(null=True, blank=True)
    emp_date_hired = models.DateTimeField(null=True, blank=True)
    emp_history = models.CharField(null=True, blank=True, max_length=12)
    emp_wave_no = models.CharField(null=True, blank=True, max_length=12)
    emp_team = models.CharField(null=True, blank=True, max_length=30)
    emp_leave_credit = models.IntegerField(null=True, blank=True)
    profile_pic = models.FileField(blank=True, default='1.jpeg')

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_id) + "-" + self.emp_firstname
        #     return str(self.emp_id) + "  " + self.emp_firstname + "  " + str(self.emp_position_ID)


# holds shift schedule
class EmployeeSchedule(models.Model):
    emp_shift_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('EmployeeDetail', on_delete=None)
    emp_shift_code = models.CharField(max_length=20, blank=True, null=True)
    start_schedule_time = models.TimeField(blank=True, null=True)
    start_schedule_date = models.DateField(blank=True, null=True)
    end_schedule_time = models.TimeField(blank=True, null=True)
    end_schedule_date = models.DateField(blank=True, null=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_id) + "-" + str(self.start_schedule_time) + "  " + str(self.start_schedule_date)


# holds time in and time out
class TimeTracker(models.Model):
    time_tracker_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('EmployeeDetail', on_delete=None)
    emp_shift_code = models.CharField(max_length=20, blank=True, null=True)

    time_in_date = models.DateField(null=True, blank=True)
    time_in = models.TimeField(null=True, blank=True)
    time_out_date = models.DateField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    time_in_lunch = models.TimeField(null=True, blank=True)
    time_out_lunch = models.TimeField(null=True, blank=True)
    time_in_break = models.TimeField(null=True, blank=True)
    time_out_break = models.TimeField(null=True, blank=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    action_flag = models.CharField(max_length=5, null=True, blank=True)
    status = models.IntegerField(default='01')

    def get_absolute_url(self):
        return reverse('dashboard:dashboard', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.emp_id) + "  " + str(self.time_in_date) + "  " + str(self.time_in)


# hold ADP summary
class EmployeeAdpReport(models.Model):
    adp_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('EmployeeDetail', on_delete=None)

    l_wop = models.IntegerField(blank=True, null=True)
    tardy = models.IntegerField(blank=True, null=True)
    under_time = models.IntegerField(blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)
    night_dif = models.IntegerField(blank=True, null=True)
    legal_holiday = models.IntegerField(blank=True, null=True)
    legal_holiday_nd = models.IntegerField(blank=True, null=True)
    legal_holiday_ot = models.IntegerField(blank=True, null=True)
    legal_holiday_rdnd = models.IntegerField(blank=True, null=True)
    legal_holiday_rdot = models.IntegerField(blank=True, null=True)
    special_holiday = models.IntegerField(blank=True, null=True)
    special_holiday_nd = models.IntegerField(blank=True, null=True)
    special_holiday_ot = models.IntegerField(blank=True, null=True)
    special_holiday_rdnd = models.IntegerField(blank=True, null=True)
    special_holiday_rdot = models.IntegerField(blank=True, null=True)

    pay_cycle_from = models.DateField(blank=True, null=True)
    pay_cycle_to = models.DateField(blank=True, null=True)

    created_by = models.CharField(max_length=30, null=True, blank=True)
    created_date_time = models.DateTimeField(null=True, blank=True)
    change_by = models.CharField(max_length=30, null=True, blank=True)
    change_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_id)


# Motime Logs of action
class MotimeLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('EmployeeDetail', on_delete=None)
    time_action = models.TimeField(null=True, blank=True)
    date_action = models.DateField(null=True, blank=True)
    user_action = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(default='01')

    def __str__(self):
        return str(self.emp_id) + "  " + str(self.user_action)
