from django.conf.urls import include, url
from django.contrib import admin

from web_application import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='templates/index'),
]
