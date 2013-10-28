from django.conf.urls import patterns, include, url

from .views import GameDetailView


urlpatterns = patterns('',
    url(
        r'^(?P<slug>[\w/-]+)/$',
        GameDetailView.as_view(),
        name='detail'
    ),
)
