from django.conf.urls import patterns, include, url

from .views import RoundListView


urlpatterns = patterns('',
    url(
        r'^(?P<slug>[\w-]+)/rounds/$',
        RoundListView.as_view(),
        name='rounds'
    ),
)
