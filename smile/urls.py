from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'common.views.home', name='home'),

                       (r'^i18n/', include('django.conf.urls.i18n')),
)
