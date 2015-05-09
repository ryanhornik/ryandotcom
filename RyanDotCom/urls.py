from django.conf.urls import patterns, include, url
from django.contrib import admin
import RyanMain.urls

urlpatterns = patterns('',

    url(r'^$', include(RyanMain.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
