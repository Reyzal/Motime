import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmployeeTimeSched
from django.http import JsonResponse
from dashboard.models import EmployeeDetail


# Create your views here.
@login_required(login_url='login:login')
def timesched_view(request):
    if request.user.is_authenticated():
        emp_id = request.user.emp_id
        emp_detail = EmployeeDetail.objects.get(emp_id=emp_id)

        context = {'emp_detail': emp_detail}
        return render(request, 'timesched.html', context)
