from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import Game


class GameDetailView(DetailView):
    model = Game
    slug_field = 'long_slug'

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        game = get_object_or_404(Game, long_slug=self.kwargs.get('slug'))

        # Filtering teams to get only players of the selected league
        team_home_players = game.team_home.teamplayer_set.filter(
            league=game.game_round.league
        )
        team_away_players = game.team_away.teamplayer_set.filter(
            league=game.game_round.league
        )
        context['team_home_players'] = team_home_players
        context['team_away_players'] = team_away_players

        return context
