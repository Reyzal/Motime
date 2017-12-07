from django.http import *

import datetime
from .forms import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dashboard.models import EmployeeDetail, EmployeeSchedule
from django.shortcuts import render
from dashboard.models import TimeTracker, MotimeLogs
from django.core.files.storage import FileSystemStorage


# This is all for change password view
@login_required(login_url='login:login')
def change_view(request):
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

        # check if user is already clocked in
        action = '0'  # initialize

        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
            action = timetrack.action_flag

        elif TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=previous_date)
            action = timetrack.action_flag

        template = 'registration/change_password.html'
        context = {'emp_detail': emp_detail,
                   'action_flag': action}

        return render(request, template, context)


@login_required(login_url='login:login')
def change_password(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        if request.method == 'POST':
            password = request.POST.get('password')

            # u = CustomUser.objects.get(username=emp_detail.emp_email)
            # u.set_password(password)
            # u.save()

            data = {'result': 'You have change your password'}
            return JsonResponse(data)
        else:
            data = {'result': 'This is not a get function'}
            return JsonResponse(data)

    data = {'result': '',
            'error': ' not authenticated'}
    JsonResponse(data)


@login_required(login_url='login:login')
def validate_password(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id

        user_details = CustomUser.objects.get(emp_id=emp_id)
        user_detail_password = user_details.password
        user_password = request.GET.get('password')

        template = 'registration/change_password.html'
        context = {'passworddb': user_detail_password,
                   'passwordajax': user_password}

        return render(request, template, context)

        # if user_detail_password == user_password:
        # data = {
        #     'is_correct': True,
        #     'error': 'failed to validate password'
        # }
        # return JsonResponse(data)


# end of change password view

# account settings view
@login_required(login_url='login:login')
def accout_settings(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

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

        if emp_detail.emp_status == 0:
            emp_status = 'Provisionary'
        else:
            emp_status = 'Regular'

        if emp_detail.emp_gender == 'M':
            emp_gender = 'Male'
        else:
            emp_gender = 'Female'

        emp_position = str(emp_detail.emp_position_ID)
        position_id, position_desc = emp_position.split("-")

        emp_department = str(emp_detail.emp_department_ID)
        department_id, department_desc = emp_department.split("-")

        # check if user is already clocked in
        action = '0'  # initialize

        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
            action = timetrack.action_flag

        elif TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=previous_date)
            action = timetrack.action_flag

        context = {'emp_detail': emp_detail,
                   'emp_status': emp_status,
                   'emp_gender': emp_gender,
                   'emp_position': position_desc,
                   'emp_department': department_desc,
                   'action_flag': action,
                   }

        return render(request, 'registration/acccount_settings.html', context)


@login_required(login_url='login:login')
def update_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ''

            # if request.method == 'POST' and request.FILES['myfile']:
            #     emp_id = request.user.emp_id
            #     myfile = request.FILES['myfile']
            #     fs = FileSystemStorage()
            #     filename = fs.save(myfile.name, myfile)
            #
            #     # emp_profile_pic = request.POST.get('profile_pic')
            #
            #     EmployeeDetail.objects.filter(emp_id=emp_id).update(
            #         profile_pic=filename,
            #     )
            #
            #     data = {'result': 'You have Succesfully updated profile pic',
            #             'error': 'Failed to upload'
            #             }
            #     return JsonResponse(data)
            #     data = {'error': 'POST Request failed'}
            #     return JsonResponse(data)
            # data = {'error': 'not authenticated'}
            # return JsonResponse(data)


# end of account settings view

# this is for initial page view
@login_required(login_url='login:login')
def initial_view(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()
        # get date time to be formated
        h = str(date.hour)
        mi = str(date.minute)
        s = str(date.second)

        d = str(date.day)
        y = str(date.year)
        mo = str(date.month)

        if d < '10':
            d = '0' + d

        if mo < '10':
            mo = mo + '0'

        date_now = y + '-' + mo + '-' + d

        fullmonth_name = ''
        if mo == '1':
            fullmonth_name = 'January'
        elif mo == '2':
            fullmonth_name = 'February'
        elif mo == '3':
            fullmonth_name = 'March'
        elif mo == '4':
            fullmonth_name = 'March'
        elif mo == '5':
            fullmonth_name = 'April'
        elif mo == '6':
            fullmonth_name = 'May'
        elif mo == '7':
            fullmonth_name = 'June'
        elif mo == '8':
            fullmonth_name = 'July'
        elif mo == '9':
            fullmonth_name = 'August'
        elif mo == '10':
            fullmonth_name = 'September'
        elif mo == '11':
            fullmonth_name = 'November'
        elif mo == '12':
            fullmonth_name = 'December'

        time = h + ':' + mi + ':' + s
        hours, minutes, seconds = time.split(":")
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        setting = "AM"
        if hours > 12:
            setting = "PM"
            h = int(hours)
            h -= 12

        converted_time = str(h) + ':' + str(minutes) + ' ' + setting
        current_date = fullmonth_name + '  ' + d + ', ' + y
        timestamp = current_date + ' ' + converted_time

        # Check if user is existing and is is the schedule

    context = {}
    return render(request, 'registration/initial.html', context)


def timeConvert(time):
    h = ''

    miliTime = time
    hours, minutes, seconds = miliTime.split(":")
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)

    h = hours

    setting = "AM"
    if hours > 12:
        setting = "PM"
        h = int(hours)
        h -= 12

    return str(h) + ':' + str(minutes) + '0' + ' ' + setting


# end of initial page view

# all custom login, logout view
@login_required(login_url='login:login')
def logout_view(request):
    logout(request)
    context = {}
    return render(request, 'registration/login.html', context)
    # end of custom login, logout view


@login_required(login_url='login:login')
def clock_in(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        formated_date = date.strftime('%Y-%m-%d')
        emp_sched = EmployeeSchedule.objects.get(emp_id=emp_id, start_schedule_date=formated_date)

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

        current_date = y + '-' + mo + '-' + str(days)
        timestamp = current_date + ' ' + time

        # can only time in onces per day
        if not TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            # create clockin record
            emp_clockin = TimeTracker(
                emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                time_in_date=current_date,
                time_in=time,
                emp_shift_code=emp_sched.emp_shift_code,
                action_flag='01',
                created_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                created_date_time=timestamp,
            )
            emp_clockin.save()

            # create log record
            action = request.POST.get('action')
            logs = MotimeLogs(
                emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                time_action=time,
                date_action=current_date,
                user_action='Clock In'
            )
            logs.save()

        # this will call dashboard
        action = '0'  # initialize
        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
            action = timetrack.action_flag

        # check user role
        postion_id, postion_desc = str(emp_detail.emp_position_ID).split("-")

        if int(postion_id) != 1004 and int(postion_id) != 1002:
            tardy = 0
            overtime = 0
            undertime = 0
            lwop = 0
            night_dif = 0

            context = {'emp_detail': emp_detail,
                       'tardy': tardy,
                       'overtime': overtime,
                       'undertime': undertime,
                       'lwop': lwop,
                       'night_dif': night_dif,
                       'action_flag': action}

            template = 'dashboard.html'
            return render(request, template, context)
        else:
            template = 'dashboard_opl.html'
            context = {'emp_detail': emp_detail,
                       'id': emp_detail.emp_position_ID,
                       'action_flag': action}
            return render(request, template, context)
