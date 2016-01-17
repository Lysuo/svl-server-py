from django.conf.urls import include, url
from django.contrib import admin
import inputformsapp.views as v

urlpatterns = [ 
    url(r'^$', v.home, name='home'),
    url(r'^angular/?$', v.angular, name='angular'),
]
