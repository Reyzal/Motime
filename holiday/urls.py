from django.conf.urls import url
from . import views

app_name = 'holiday'

urlpatterns = [
    url(r'^$', views.holiday_view, name='holiday'),
]
