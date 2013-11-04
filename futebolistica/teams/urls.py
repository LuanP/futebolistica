from django.conf.urls import patterns, include, url

from .views import TeamListView, TeamDetailView


urlpatterns = patterns('',
    url(r'^$', TeamListView.as_view(), name='list'),
    url(r'^(?P<slug>[-\w]+)/$', TeamDetailView.as_view(), name='detail'),
)
