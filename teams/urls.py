from django.conf.urls import patterns, include, url

from .views import TeamListView


urlpatterns = patterns('',
    url(r'^$', TeamListView.as_view(), name='list'),
)
