from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import League, Round


class LeagueListView(ListView):
    model = League


class RoundListView(ListView):
    model = Round

    def get_context_data(self, **kwargs):
        context = super(RoundListView, self).get_context_data(**kwargs)
        context['league'] = get_object_or_404(
            League,
            slug=self.kwargs.get('slug')
        )
        return context

    def get_queryset(self):
        qs = super(RoundListView, self).get_queryset()
        qs = qs.filter(league__slug=self.kwargs.get('slug'))
        return qs
