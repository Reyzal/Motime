from django.conf.urls import url, include
from . import views

app_name = 'overtime'

urlpatterns = [
    url(r'^$', views.overtime_view, name='overtime'),
    url(r'^ajax/overtime_create/$', views.overtime_create, name='overtime_create'),
    url(r'^ajax/overtime_table/$', views.load_table_ot, name='overtime_table'),

    url(r'^overtime-opl$', views.overtime_view_opl, name='overtime-opl'),
]
