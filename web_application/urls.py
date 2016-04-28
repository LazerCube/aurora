from django.conf.urls import include, url
from django.contrib import admin

from web_application import views
from friends import views as friends


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='user_profile'),
    url(r'^friends/$', friends.view_friends, name='view_friends'),
    url(r'^friend/add/(?P<to_username>[\w.@+-]+)$', friends.add_friends, name='add_friend'),
    url(r'^friend/requests/(?P<friendship_request_id>\d+)/cancel/$', friends.cancel_friends, name='cancel_friends'),
    url(r'^friend/requests/(?P<friendship_request_id>\d+)/accept/$', friends.accept_friends, name='accept_friends'),
    url(r'^friend/requests/(?P<friendship_request_id>\d+)/reject/$', friends.reject_friends, name='reject_friends'),
    url(r'^friend/requests/$', friends.view_requests, name='view_requests'),
    url(r'^$', views.index, name='index'),
]
