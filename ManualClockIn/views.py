import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ManualClockIn
from dashboard.models import EmployeeDetail, TimeTracker
from django.http import JsonResponse


@login_required(login_url='login:login')
def ManualClockIn(request):
    if request.user.is_authenticated():
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)
        manual = '' #ManualClockIn.objects.get(emp_id=emp_id)

        action = '0'  # initialize

        schedule = ''

        context = {'emp_detail': emp_detail,
                   'action_flag': action,
                   'manual': manual,
                   'schedule': schedule}

        return render(request, 'ManualClockIn.html', context)
