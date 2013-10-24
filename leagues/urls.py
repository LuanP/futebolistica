from django.conf.urls import patterns, include, url

from .views import LeagueListView


urlpatterns = patterns('',
    url(r'^$', LeagueListView.as_view(), name='list'),
)
