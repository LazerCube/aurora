from django.conf.urls import include, url
from django.contrib import admin

from web_application import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='user_profile'),
    url(r'^friends/', include('friends.urls')),
    url(r'^$', views.index, name='index'),
]
