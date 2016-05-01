from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^', include('authentication.urls')),
    url(r'^', include('user_profiles.urls')),
    url(r'^friends/', include('friends.urls')),
    url(r'^messages/', include('chat.urls')),
    url(r'^$', views.index, name='index'),
]
