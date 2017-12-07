from django.contrib import admin
from .models import EmployeePosition, EmployeeDetail, TimeTracker, EmployeeSchedule, EmployeeAdpReport, \
    EmployeeDepartment, MotimeLogs

# Register your models here.
admin.site.register(EmployeePosition)
admin.site.register(EmployeeDetail)
admin.site.register(TimeTracker)
admin.site.register(EmployeeSchedule)
admin.site.register(EmployeeAdpReport)
admin.site.register(EmployeeDepartment)
admin.site.register(MotimeLogs)

