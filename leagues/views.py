from django.views.generic import ListView

from .models import League


class LeagueListView(ListView):
    model = League
