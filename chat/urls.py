from django.conf.urls import include, url
from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.view_chatrooms, name='view_chatrooms'),
]
