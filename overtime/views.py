import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmployeeOvertime
from django.http import JsonResponse
from dashboard.models import EmployeeDetail, TimeTracker


@login_required(login_url='login:login')
def overtime_view(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

        emp_id = request.user.emp_id
        emp_ot = EmployeeOvertime.objects.all()
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

        emp_ot = ''
        if EmployeeOvertime.objects.filter(emp_id=emp_id).exists():
            emp_ot = EmployeeOvertime.objects.filter(emp_id=emp_id)

            context = {'emp_ot': emp_ot,
                       'emp_detail': emp_detail,
                       'action_flag': action}

            return render(request, 'overtime.html', context)
        else:
            context = {'emp_ot': emp_ot,
                       'emp_detail': emp_detail,
                       'action_flag': action}

            return render(request, 'overtime.html', context)


@login_required(login_url='login:login')
def overtime_create(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

        data = {}

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
            ot_date = request.POST.get('ot_date')
            ot_type = request.POST.get('ot_type')
            ot_hrs = request.POST.get('ot_hrs')

            emp_id = request.user.emp_id
            emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

            emp_ot = EmployeeOvertime(emp_id=emp_detail, ot_date=ot_date, ot_type=ot_type,
                                      ot_approved_desc='Pending Approval OPL', ot_hrs=ot_hrs,
                                      ot_date_request=current_date, created_by=emp_detail, created_date_time=timestamp)
            emp_ot.save()

            data = {'result': 'You have Succesfully requested Overtime'}
            return JsonResponse(data)

        data = {
            # 'result': 'Created Overtime successfully',
            'error': 'Failed to Create Overtime'
        }

        return JsonResponse(data)


@login_required(login_url='login:login')
def load_table_ot(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_ot = EmployeeOvertime.objects.all().filter(emp_id=emp_id)

        # data = {}
        data = []
        ot_type = []
        ot_date = []
        ot_hrs = []
        ot_date_request = []
        ot_approved = []

        for ot in emp_ot:
            data = ot

            # data = {
            #     'ot_type': ot_type.append(ot.ot_type),
            #     'ot_date': ot_date.append(ot.ot_date),
            #     'ot_hrs': ot_hrs.append(ot.ot_hrs),
            #     'ot_date_request': ot_date_request.append(ot.ot_date_request),
            #     'ot_approved': ot_approved.append(ot.ot_approved),
            # }
            # return JsonResponse(dict(data=ot_type) for type in ot_type)

            return JsonResponse(data)


# [dict(mpn=pn) for pn in lst]


@login_required(login_url='login:login')
def overtime_view_opl(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_ot = EmployeeOvertime.objects.all()
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        context = {'emp_ot': emp_ot,
                   'emp_detail': emp_detail}
        return render(request, 'overtime_opl.html', context)
