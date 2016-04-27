from django.conf.urls import include, url
from django.contrib import admin

from web_application import views
from friends import views as friends


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(?P<slug>[\w.@+-]+)/$', views.profile, name='user_profile'),
    url(r'^profile/(?P<username>[\w.@+-]+)/friends$', friends.view_friends, name='view_friends'),
    url(r'^profile/(?P<username>[\w.@+-]+)/requests$', friends.view_requests, name='view_requests'),
    url(r'^profile/(?P<username>[\w.@+-]+)/add$', friends.add_friends, name='add_friends'),
    url(r'^$', views.index, name='index'),
]
