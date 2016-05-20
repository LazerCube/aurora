from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^', include('authentication.urls')),
    url(r'^', include('user_profiles.urls')),
    url(r'^', include('news_feed.urls')),
    url(r'^friends/', include('friends.urls')),
    url(r'^messages/', include('chat.urls')),
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'web_application.views.handler403'
handler404 = 'web_application.views.handler404'
handler500 = 'web_application.views.handler505'
