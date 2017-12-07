import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmployeeDetail, EmployeeSchedule, TimeTracker, MotimeLogs
from logs.models import EmployeeLogs
from holiday.models import Holiday
from overtime.models import EmployeeOvertime
from django.http import JsonResponse


# dashboard view
@login_required(login_url='login:login')
def index_view(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        # Checker to make sure employeesched is not empty
        d = str(date.day)
        y = str(date.year)
        mo = str(date.month)

        current_date = y + '-' + mo + '-' + d

        action = '0'  # initialize
        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            timetrack = TimeTracker.objects.get(emp_id=emp_id, time_in_date=current_date)
            action = timetrack.action_flag

        # check user role
        postion_id, postion_desc = str(emp_detail.emp_position_ID).split("-")

        # Normal Position
        if int(postion_id) == 1005:
            tardy = 0
            overtime = 0
            undertime = 0
            lwop = 0
            night_dif = 0

            # Check if user has logs
            motime_log = ''
            if MotimeLogs.objects.filter(emp_id=emp_id).exists():
                motime_log = MotimeLogs.objects.filter(emp_id=emp_id)

            context = {'emp_detail': emp_detail,
                       'tardy': tardy,
                       'overtime': overtime,
                       'undertime': undertime,
                       'lwop': lwop,
                       'night_dif': night_dif,
                       'logs': motime_log,
                       'action_flag': action}

            template = 'dashboard.html'
            return render(request, template, context)

        # HR Position
        elif int(postion_id) == 1000:
            # Check if user has logs
            motime_log = ''
            if MotimeLogs.objects.filter(emp_id=emp_id).exists():
                motime_log = MotimeLogs.objects.filter(emp_id=emp_id)

            context = {'emp_detail': emp_detail,
                       'action_flag': action}

            template = 'dashboard_hr.html'
            return render(request, template, context)

        # Workforce Position
        elif int(postion_id) == 1002:
            # Check if user has logs
            motime_log = ''
            if MotimeLogs.objects.filter(emp_id=emp_id).exists():
                motime_log = MotimeLogs.objects.filter(emp_id=emp_id)

            context = {'emp_detail': emp_detail,
                       'action_flag': action}

            template = 'dashboard_workforce.html'
            return render(request, template, context)

        # lead Position
        elif int(postion_id) == 1003 or int(postion_id) == 1004:
            if MotimeLogs.objects.filter(emp_id=emp_id).exists():
                motime_log = MotimeLogs.objects.filter(emp_id=emp_id)

            template = 'dashboard_opl.html'
            context = {'emp_detail': emp_detail,
                       'id': emp_detail.emp_position_ID,
                       'action_flag': action}
            return render(request, template, context)

        elif int(postion_id) == 0:
            if MotimeLogs.objects.filter(emp_id=emp_id).exists():
                motime_log = MotimeLogs.objects.filter(emp_id=emp_id)

            template = 'dashboard.html'
            context = {'emp_detail': emp_detail,
                       'id': emp_detail.emp_position_ID,
                       'action_flag': action}

            return render(request, template, context)


@login_required(login_url='login:login')
def opl_view(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        template = 'dashboard_opl.html'
        context = {'emp_detail': emp_detail,
                   'id': emp_detail.emp_position_ID}
        return render(request, template, context)


@login_required(login_url='login:login')
def log_summary_view(request):
    log_summary = EmployeeLogs.objects.all()
    for log in log_summary:
        context = {'log': log}
        return render(request, 'dashboard.html', context)


@login_required(login_url='login:login')
def adp_view(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        template = 'adp.html'
        context = {'emp_detail': emp_detail, }

        return render(request, template, context)


@login_required(login_url='login:login')
def hr_view(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        template = 'dashboard_hr.html'

        context = {'emp_detail': emp_detail}
        return render(request, template, context)


@login_required(login_url='login:login')
def emp_detail_view(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        template = 'dashboard_hr.html'


# user time keeping
@login_required(login_url='login:login')
def ClockIn(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

        # set time and date
        h = str(date.hour)
        mi = str(date.minute)
        s = str(date.second)

        d = str(date.day)
        y = str(date.year)
        mo = str(date.month)
        time = h + ':' + mi + ':' + s

        current_date = y + '-' + mo + '-' + d
        timestamp = current_date + ' ' + time

        # get user Employee ID
        emp_id = request.user.emp_id

        # check if action is a POST
        if request.method == 'POST':
            # get user Action
            action = request.POST.get('action')

            # Check employee if he/she has has work
            if EmployeeSchedule.objects.filter(emp_id=emp_id, start_schedule_date=current_date).exists():
                data = {'result': 'Work',
                        'error': 'Noo'}
                return JsonResponse(data)

            # Employee Rest Day
            else:
                # check if user has an approved OT
                if EmployeeOvertime.objects.filter(emp_id=emp_id, start_schedule_date=current_date).exists():
                    # check if today is holiday
                    if Holiday.objects.filter(holiday_date=current_date).exists():
                        # create time in record
                        emp_clockin = TimeTracker(
                            emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                            time_in_date=current_date,
                            time_in=time,
                            emp_shift_code='Rest Day',
                            action_flag='01',
                            created_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                            created_date_time=timestamp,
                        )
                        emp_clockin.save()

                        # create summary log record
                        logs = MotimeLogs(
                            emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                            time_action=time,
                            date_action=current_date,
                            user_action=action
                        )
                        logs.save()

                        # create log for detail log record
                        detail_logs = EmployeeLogs(
                            emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                            log_action=action,
                            log_date=current_date,
                            log_time=time,
                            # total_late=0,
                            # undertime=0,
                            created_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                            created_date_time=timestamp,

                            # log_out=,
                            # start_break=,
                            # end_break=,
                            # overtime=,
                            # night_def=
                            # lwop =
                        )
                        detail_logs.save()
                    else:
                        action = ''
                else:
                    action = ''

            data = {'result': 'Rest Day',
                    'error': 'Noo'}
            return JsonResponse(data)

    # Check employee schedule
    # if EmployeeSchedule.objects.get(emp_id=emp_id, start_schedule_date=current_date):
    #     data = {'result': 'yess',
    #             'error': 'Noo'}
    #     return JsonResponse(data)
    # else:
    #     data = {'result': 'yess',
    #             'error': 'Noo'}
    #     return JsonResponse(data)

    # OLD CODE
    # if request.user.is_authenticated():
    #     date = datetime.datetime.now()
    #
    #     # get data from db
    #     emp_id = request.user.emp_id
    #     formated_date = date.strftime('%Y-%m-%d')
    #     emp_sched = EmployeeSchedule.objects.get(emp_id=emp_id, start_schedule_date=formated_date)
    #
    #     # set time for format has needed
    #     h = str(date.hour)
    #     mi = str(date.minute)
    #     s = str(date.second)
    #
    #     d = str(date.day)
    #     y = str(date.year)
    #     mo = str(date.month)
    #     time = h + ':' + mi + ':' + s
    #
    #     # this is a filter for 12:00 AM schedules
    #     if time == '00:00:00':
    #         days = date.day - 1
    #     else:
    #         days = d
    #
    #     current_date = y + '-' + mo + '-' + str(days)
    #     timestamp = current_date + ' ' + time
    #
    #     # process POST request
    #     if request.method == 'POST':
    #         # create time in record
    #         emp_clockin = TimeTracker(
    #             emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
    #             time_in_date=current_date,
    #             time_in=time,
    #             emp_shift_code=emp_sched.emp_shift_code,
    #             action_flag='01',
    #             created_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
    #             created_date_time=timestamp,
    #         )
    #         emp_clockin.save()
    #
    #         # create summary log record
    #         action = request.POST.get('action')
    #         logs = MotimeLogs(
    #             emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
    #             time_action=time,
    #             date_action=current_date,
    #             user_action=action
    #         )
    #         logs.save()
    #
    #         # create log for detail log record
    #         detail_logs = EmployeeLogs(
    #             emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
    #             log_action=action,
    #             log_date=current_date,
    #             log_time=time,
    #             # total_late=0,
    #             # undertime=0,
    #             created_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
    #             created_date_time=timestamp,
    #
    #             # log_out=,
    #             # start_break=,
    #             # end_break=,
    #             # overtime=,
    #             # night_def=
    #             # lwop =
    #         )
    #         detail_logs.save()
    #
    #         data = {'result': 'You have Succesfully clock in'}
    #         return JsonResponse(data)


@login_required(login_url='login:login')
def ClockOut(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

        # get data from db
        emp_id = request.user.emp_id

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
        previous_date = y + '-' + mo + '-' + d

        timestamp = current_date + ' ' + time

        # check if user is clock in  for the morning shift
        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).update(
                time_out_date=current_date,
                time_out=time,
                change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                change_date=timestamp,
                action_flag='04'
            )

            # create log record
            action = request.POST.get('action')
            logs = MotimeLogs(
                emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                time_action=time,
                date_action=current_date,
                user_action=action
            )
            logs.save()

            # update log for detail log record
            detail_logs = EmployeeLogs.objects.filter(emp_id=emp_id, log_date=current_date).update(
                log_out=time,
                night_def=0,
                change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                change_date=timestamp,
            )

            # total_late='',
            # undertime='',
            # log_time=,
            # start_break=,
            # end_break=,
            # overtime=,
            # night_def=
            # lwop =

        # check if user is clock in  for the night shift
        elif TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).exists():

            TimeTracker.objects.filter(emp_id=emp_id, time_in_date=previous_date).update(
                time_out_date=current_date,
                time_out=time,
                change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                change_date=timestamp,
                action_flag='04'
            )

            # create log record
            action = request.POST.get('action')
            logs = MotimeLogs(
                emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                time_action=time,
                date_action=current_date,
                user_action=action
            )
            logs.save()

            # update log for detail log record
            detail_logs = EmployeeLogs.objects.filter(emp_id=emp_id, log_date=previous_date).update(
                log_out=time,
                night_def='',
                change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                change_date=timestamp,
            )

        data = {'result': 'You have Succesfully clock out'}
        return JsonResponse(data)


@login_required(login_url='login:login')
def LunchIn(request):
    if request.user.is_authenticated:
        date = datetime.datetime.now()

        # get data from db
        emp_id = request.user.emp_id

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
        previous_date = y + '-' + mo + '-' + d

        timestamp = current_date + ' ' + time

        if TimeTracker.objects.filter(emp_id=emp_id, time_in_date=current_date).exists():
            TimeTracker.objects.filter(time_in_date=current_date, emp_id=emp_id).update(
                time_in_lunch=time,
                change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                change_date=timestamp,
                action_flag='02'
            )

            # create log record
            action = request.POST.get('action')
            logs = MotimeLogs(
                emp_id=EmployeeDetail.objects.get(emp_id=emp_id),
                time_action=time,
                date_action=current_date,
                user_action=action
            )
            logs.save()

            # update log for detail log record
            detail_logs = EmployeeLogs.objects.filter(emp_id=emp_id, log_date=current_date).update(
                start_break=time,
                change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                change_date=timestamp,
            )

        data = {'result': 'You have started your break'}
        return JsonResponse(data)

        # if TimeTracker.objects.filter(time_in_date=current_date, emp_id=emp_id).exists():
        #     # update
        #     TimeTracker.objects.filter(time_in_date=current_date, emp_id=emp_id).update(
        #         time_in_lunch=time,
        #         change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
        #         change_date=timestamp,
        #     )

        # context = {}
        # return render(request, 'dashboard.html', context)


@login_required(login_url='login:login')
def LunchOut(request):
    date = datetime.datetime.now()

    if request.user.is_authenticated:
        emp_id = request.user.emp_id

        h = str(date.hour)
        mi = str(date.minute)
        s = str(date.second)

        y = str(date.year)
        mo = str(date.month)
        d = str(date.day)

        time = h + ':' + mi + ':' + s

        # this is a filter for 12:00 AM schedules
        if time == '00:00:00':
            days = date.day - 1

        d = str(days)
        current_date = y + '-' + mo + '-' + d
        timestamp = current_date + ' ' + time

        if TimeTracker.objects.filter(time_in_date=current_date, emp_id=emp_id).exists():
            # update
            TimeTracker.objects.filter(time_in_date=current_date, emp_id=emp_id).update(
                time_out_lunch=time,
                change_by=str(EmployeeDetail.objects.get(emp_id=emp_id)),
                change_date=timestamp,
            )

    context = {}
    return render(request, 'dashboard.html', context)

# end of user time keeping
