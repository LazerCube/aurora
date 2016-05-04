from django.conf.urls import include, url
from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.view_chatrooms, name='view_chatrooms'),
    url(r'^conversation/(?P<chatroom_id>\d+)$', views.view_chat, name='view_chat'),
    url(r'^conversation/send$', views.send, name='send'),
    url(r'^conversation/receive$', views.receive, name='receive'),
    url(r'^conversation/sync$', views.sync, name='sync'),
]
