from django.views.generic import DetailView

from .models import Game


class GameDetailView(DetailView):
    model = Game
    slug_field = 'long_slug'
