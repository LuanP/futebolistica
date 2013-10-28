from django.views.generic import ListView, DetailView

from .models import Team


class TeamListView(ListView):
    model = Team


class TeamDetailView(DetailView):
    model = Team
