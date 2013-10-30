from django.views.generic import ListView, DetailView

from leagues.models import League
from .models import Team


class TeamListView(ListView):
    model = Team


class TeamDetailView(DetailView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['players_by_league'] = []
        for league in League.objects.all():
            teamplayers = league.teamplayer_set.filter(
                team__slug=self.kwargs.get('slug')
            )
            context['players_by_league'].append([league.name, teamplayers])
        return context
