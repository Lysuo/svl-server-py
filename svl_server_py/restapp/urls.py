from django.conf.urls import patterns, include, url
from django.contrib import admin

from restapp import views

urlpatterns = patterns('restapp.views',

    url(r'^languages/$', views.LanguageList.as_view()),
    url(r'^types/$', views.TypeList.as_view()),
    url(r'^chapters/$', views.ChapterList.as_view()),
    url(r'^words/$', views.WordList.as_view()),
)
