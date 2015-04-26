from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('inputformsapp.views',

    url(r'^$', 'home', name='home'),
    url(r'^angular/?$', 'angular', name='angular'),
)
