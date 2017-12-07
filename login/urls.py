from django.conf.urls import url, include
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm
from django.contrib.auth import views as auth_views
from django.contrib.sites.models import Site
# from django.core.urlresolvers import reverse_lazy

from . import views

app_name = 'login'

urlpatterns = [
    # authentications pages
    url(r'^$', views.initial_view, name='initial'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^account/change-password$', views.change_view, name='change_password'),

    url(r'^account/settings/$', views.accout_settings, name='account_settings'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^validate_password/$', views.validate_password, name='validate_password'),
    url(r'^update_password/$', views.change_password, name='update_password'),

    url(r'^clockin/$', views.clock_in, name='clockin'),
    url('^', include('django.contrib.auth.urls')),

    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    #
    #
    # url(r'^password_reset/done$', auth_views.password_reset_done,
    #     {'post_reset_redirect': reverse_lazy('auth_password_reset_done'),
    #      'extra_email_context': {'site': Site.objects.get_current()}},
    #     name='password_reset/done'),
    #
    #
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    #
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
