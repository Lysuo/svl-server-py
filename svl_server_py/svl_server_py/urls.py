from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [ 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('inputformsapp.urls')),
    url(r'^api/rest/', include('restapp.urls')),
    url(r'^signin/', views.connect, name="connect"),
    url(r'^signout/', views.disconnect, name="disconnect"),
]

# useful in debug mode so that Django server can serve static files
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
