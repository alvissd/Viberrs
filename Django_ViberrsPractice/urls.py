from django.conf.urls import include,url
from django.contrib import admin
from music import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^music/',include('music.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
    