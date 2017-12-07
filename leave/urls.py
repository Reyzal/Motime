from django.conf.urls import url
from . import views

app_name = 'leave'

urlpatterns = [
    url(r'^$', views.leave_view, name='leave'),
    url(r'^leave_opl$', views.leave_view_opl, name='leave_opl$'),
    url(r'^ajax/leave_create/$', views.leave_create, name='leave_create'),
]
