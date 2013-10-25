from django.conf.urls import patterns, include, url

from .views import LeagueListView, RoundListView


urlpatterns = patterns('',
    url(r'^$', LeagueListView.as_view(), name='list'),
    url(
        r'^(?P<slug>[\w-]+)/rounds/$',
        RoundListView.as_view(),
        name='rounds'
    ),
)
