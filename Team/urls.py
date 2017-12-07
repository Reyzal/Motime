from django.conf.urls import url
from . import views

app_name = 'team'

urlpatterns = [
    url(r'^$', views.team_view, name='team'),
]
