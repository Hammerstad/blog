from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)