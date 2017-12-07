import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmployeeLogs
from dashboard.models import EmployeeDetail, TimeTracker


# Create your views here.
@login_required(login_url='login:login')
def logs_view(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        # set time for format has needed
        h = str(date.hour)
        mi = str(date.minute)
        s = str(date.second)

        d = str(date.day)
        y = str(date.year)
        mo = str(date.month)
        time = h + ':' + mi + ':' + s

        # this is a filter for 12:00 AM schedules
        if time == '00:00:00':
            days = date.day - 1
        else:
            days = d

        # check if user is already clocked in
        action = '0'  # initialize

        current_date = y + '-' + mo + '-' + d
        previous_date = y + '-' + mo + '-' + days

        # This is for the status of clockin buttons
        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
            action = timetrack.action_flag

        elif TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=previous_date)
            action = timetrack.action_flag

        # this check if employee logs exist
        if EmployeeLogs.objects.filter(emp_id=emp_id).exists():
            emp_logs = EmployeeLogs.objects.filter(emp_id=emp_id)

            context = {'emp_detail': emp_detail,
                       'emp_logs': emp_logs,
                       'action_flag': action}

            return render(request, 'logs.html', context)
        else:
            context = {'emp_detail': emp_detail,
                       'action_flag': action}

            return render(request, 'logs.html', context)


@login_required(login_url='login:login')
def logs_view_opl(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        # set time for format has needed
        h = str(date.hour)
        mi = str(date.minute)
        s = str(date.second)

        d = str(date.day)
        y = str(date.year)
        mo = str(date.month)
        time = h + ':' + mi + ':' + s

        # this is a filter for 12:00 AM schedules
        if time == '00:00:00':
            days = date.day - 1
        else:
            days = d

        current_date = y + '-' + mo + '-' + d
        previous_date = y + '-' + mo + '-' + days

        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)
        action = '0'  # initialize

        # This is for the status of clockin buttons
        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
            action = timetrack.action_flag

        elif TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=previous_date)
            action = timetrack.action_flag

        # this check if employee logs exist
        if EmployeeLogs.objects.filter(emp_id=emp_id).exists():
            emp_logs = EmployeeLogs.objects.filter(emp_id=emp_id)

        context = {'emp_detail': emp_detail,
                   'action_flag': action}

        return render(request, 'logs_opl.html', context)
