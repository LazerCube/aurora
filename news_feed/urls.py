from django.conf.urls import include, url
from . import views

app_name = 'news_feed'
urlpatterns = [
    url(r'^$', views.home, name='index'),
]
