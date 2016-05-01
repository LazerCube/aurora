from django.conf.urls import include, url
from . import views

app_name = 'friends'
urlpatterns = [
    url(r'^$', views.view_friends, name='view_friends'),
    url(r'^requests/$', views.view_requests, name='view_requests'),
    url(r'^add/(?P<to_username>[\w.@+-]+)$', views.add_friends, name='add_friend'),
    url(r'^remove/(?P<friend_username>[\w.@+-]+)$', views.remove_friend, name='remove_friend'),
    url(r'^requests/(?P<friendship_request_id>\d+)/cancel/$', views.cancel_friends, name='cancel_friend'),
    url(r'^requests/(?P<friendship_request_id>\d+)/accept/$', views.accept_friends, name='accept_friend'),
    url(r'^requests/(?P<friendship_request_id>\d+)/reject/$', views.reject_friends, name='reject_friend'),
]
