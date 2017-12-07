from django.contrib import admin
from .models import EmployeeTeam, EmployeeTeamMembers

# Register your models here.
admin.site.register(EmployeeTeam)
admin.site.register(EmployeeTeamMembers)