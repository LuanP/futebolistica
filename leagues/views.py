from django.views.generic import ListView

from .models import League, Round


class LeagueListView(ListView):
    model = League


class RoundListView(ListView):
    model = Round

    def get_queryset(self):
        qs = super(RoundListView, self).get_queryset()
        qs = qs.filter(league__slug=self.kwargs.get('slug'))
        return qs
