from django.conf.urls import patterns, include, url
from django.contrib import admin

from restapp import views

urlpatterns = patterns('restapp.views',

    url(r'^languages/$', views.LanguageRest().as_view()),
    url(r'^types/$', views.TypeRest().as_view()),
    url(r'^chapters/$', views.ChapterRest().as_view()),
    url(r'^words/$', views.WordRest().as_view()),
)
