from django.conf.urls import include, url
from . import views

app_name = 'user_profile'
urlpatterns = [
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='index'),
]