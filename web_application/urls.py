from django.conf.urls import include, url
from django.contrib import admin

from web_application import views

urlpatterns = [
    url(r'^test_ajax/$', views.test_ajax, name='ajax'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
