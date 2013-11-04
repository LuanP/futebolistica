from django.conf.urls import patterns, include, url

from .views import HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^leagues/', include('leagues.urls', namespace='leagues')),
    url(r'^teams/', include('teams.urls', namespace='teams')),
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^admin/', include(admin.site.urls)),
)
