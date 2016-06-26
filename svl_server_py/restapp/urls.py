from django.conf.urls import include, url
from django.contrib import admin

import restapp.views as v

urlpatterns = [ 

    url(r'^languages/$', v.LanguageRest().as_view()),
    url(r'^types/$', v.TypeRest().as_view()),
    url(r'^chapters/$', v.ChapterRest().as_view()),
    url(r'^words/$', v.WordRest().as_view()),
    url(r'^dump/$', v.DumpRest().as_view()),
]
