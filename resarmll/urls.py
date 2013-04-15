from django.conf.urls import patterns, include, url
from django.contrib import admin
from hackers import urls as hackers_urls
from booking import urls as booking_urls
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(hackers_urls.urlpatterns)),
    url(r'^booking/', include(booking_urls.urlpatterns)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
