import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmployeeLeave
from django.http import JsonResponse
from dashboard.models import EmployeeDetail, TimeTracker


# Create your views here.
@login_required(login_url='login:login')
def leave_view(request):
    if request.user.is_authenticated():
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

        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
            action = timetrack.action_flag

        elif TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=previous_date)
            action = timetrack.action_flag

        emp_leave = ''
        if EmployeeLeave.objects.filter(emp_id=emp_id).exists():
            emp_leave = EmployeeLeave.objects.filter(emp_id=emp_id)

            context = {'emp_detail': emp_detail,
                       'emp_leave': emp_leave,
                       'action_flag': action}

            return render(request, 'leave.html', context)
        else:

            context = {'emp_detail': emp_detail,
                       'emp_leave': emp_leave,
                       'action_flag': action}
            return render(request, 'leave.html', context)


@login_required(login_url='login:login')
def leave_view_opl(request):
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

    if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
        timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
        action = timetrack.action_flag

    elif TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).exists():
        timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=previous_date)
        action = timetrack.action_flag

    emp_leave = ''
    if EmployeeLeave.objects.filter(emp_id=emp_id).exists():
        emp_leave = EmployeeLeave.objects.filter(emp_id=emp_id)

        context = {'emp_detail': emp_detail,
                   'emp_leave': emp_leave,
                   'action_flag': action}

        return render(request, 'leave_opl.html', context)
    else:

        context = {'emp_detail': emp_detail,
                   'emp_leave': emp_leave,
                   'action_flag': action}
        return render(request, 'leave_opl.html', context)


@login_required(login_url='login:login')
def leave_create(request):
    if request.user.is_authenticated():
        date = datetime.datetime.now()

        h = str(date.hour)
        mi = str(date.minute)
        s = str(date.second)

        d = str(date.day)
        y = str(date.year)
        mo = str(date.month)

        time = h + ':' + mi + ':' + s
        current_date = y + '-' + mo + '-' + d
        timestamp = current_date + ' ' + time

        if request.method == 'POST':
            lv_date_start = request.POST.get('lv_date_start')
            lv_date_end = request.POST.get('lv_date_end')
            lv_type = request.POST.get('lv_type')
            lv_shift = request.POST.get('lv_shift')

            lv_desc = ''
            lv_approve_desc = ''
            if lv_type == 'VL':
                lv_desc = 'Vacation Leave'
                lv_approve_desc = 'Pending Approval Workforce'
            elif lv_type == 'SL':
                lv_desc = 'Sick Leave'
                lv_approve_desc = 'Pending Approval OPL'
            elif lv_type == 'EL':
                lv_approve_desc = 'Pending Approval Workforce'
            elif lv_type == 'PL':
                lv_approve_desc = 'Pending Approval Workforce'
            elif lv_type == 'ML':
                lv_approve_desc = 'Pending Approval Workforce'

            emp_id = request.user.emp_id
            emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

            emp_lv = EmployeeLeave(emp_id=emp_detail, lv_date_start=lv_date_start, lv_date_end=lv_date_end,
                                   lv_type=lv_type, lv_desc=lv_desc, lv_approve_desc=lv_approve_desc, lv_shift=lv_shift,
                                   lv_date_request=current_date, created_by=emp_detail, created_date_time=timestamp)
            emp_lv.save()

            data = {'result': 'You have Succesfully requested Leave'}
            return JsonResponse(data)

        data = {
            'error': 'Failed to Create Leave'
        }

        return JsonResponse(data)
