from django.conf.urls import url, include
from . import views

app_name = 'timesched'

urlpatterns = [
    url(r'^$', views.timesched_view, name='timesched'),
    # url(r'^ajax/leave_create/$', views.leave_create, name='leave_create'),
]