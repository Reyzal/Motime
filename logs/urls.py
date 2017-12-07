from django.conf.urls import url
from . import views

app_name = 'logs'

urlpatterns = [
    url(r'^$', views.logs_view, name='logs'),
    url(r'^logs_opl$', views.logs_view_opl, name='logs_opl'),
]
