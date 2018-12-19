# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views, apis
from reportings import views as rep_views


urlpatterns = [
    url(r'^$', rep_views.homepage_dashboard_view, name='homepage_dashboard_view'),
    url(r'^list$', views.list_users_view, name='list_users_view'),
    #url(r'^home$', views.home, name='home'),
    url(r'^dashboard$', rep_views.homepage_dashboard_view, name='homepage_dashboard_view'),
    url(r'^details$', views.user_details_view, name='user_details_view'),
    url(r'^add$', views.add_user_view, name='add_user_view'),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^admin/', admin.site.urls),

    # REST-API Endpoints
    url(r'^users/api/v1/details/(?P<user_id>[0-9]+)$', apis.user_details_api, name='user_details_api'),
    url(r'^users/api/v1/list$', apis.list_users_api, name='list_users_api'),
    url(r'^users/api/v1/authtoken/get$', apis.get_user_authtoken, name='get_user_authtoken'),
    url(r'^users/api/v1/authtoken/renew$', apis.renew_user_authtoken, name='renew_user_authtoken'),
    url(r'^users/api/v1/authtoken/delete$', apis.delete_user_authtoken, name='delete_user_authtoken'),
]
