import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Holiday
from dashboard.models import EmployeeDetail


@login_required(login_url='login:login')
def holiday_view(request):
    if request.user.is_authenticated():
        date = datetime.datetime.now()
        emp_id = request.user.emp_id