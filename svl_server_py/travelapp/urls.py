from django.conf.urls import include, url
from django.contrib import admin
import travelapp.views as v

urlpatterns = [ 
    url(r'^travel/$', v.main, name='main'),
    url(r'^travel/(?P<slug_country>.+)/$', v.main, name='main'),
    url(r'^travel/(?P<year>\d+)/(?P<slug_country>.+)/$', v.main, name='main'),
]
