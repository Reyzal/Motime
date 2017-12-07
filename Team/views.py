import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmployeeTeamMembers, EmployeeTeam
from django.http import JsonResponse
from dashboard.models import EmployeeDetail


@login_required(login_url='login:login')
def team_view(request):
    if request.user.is_authenticated:
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        context = {'emp_detail': emp_detail}
        template = 'team_members.html'
        return render(request, template, context)
