from django.conf.urls import url
from . import views

app_name = 'manualclockin'

urlpatterns = [
    url(r'^$', views.ManualClockIn, name='manualclockin'),
]
