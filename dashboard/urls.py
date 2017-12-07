from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index_view, name='dashboard'),
    url(r'^dashboard-opl$', views.opl_view, name='dashboard-opl'),
    url(r'^dashboard-hr', views.hr_view, name='dashboard-hr'),
    url(r'^adp-view$', views.adp_view, name='adp-view'),

    url(r'^clock-in/$', views.ClockIn, name='clock-in'),
    url(r'^clock-out/$', views.ClockOut, name='clock-out'),
    url(r'^lunch-in/$', views.LunchIn, name='lunch-in'),
    url(r'^lunch-out/$', views.LunchOut, name='lunch-out'),
]
