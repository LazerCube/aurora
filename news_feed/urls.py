from django.conf.urls import include, url
from . import views

app_name = 'news_feed'
urlpatterns = [
    url(r'^home/$', views.home, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.view_post, name='view_post'),
    url(r'^post/(?P<post_id>\d+)/delete$', views.delete_post, name='delete_post'),
]
