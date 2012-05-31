from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from grabber.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls) ),
    (r'^$', main_page),
    (r'^rss/$', print_rss),
    (r'^check_new_item/$', check_new_item),    
    # Examples:
    # url(r'^$', 'jejadlepod.views.home', name='home'),
    # url(r'^jejadlepod/', include('jejadlepod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)

urlpatterns += staticfiles_urlpatterns()