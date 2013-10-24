from django.views.generic import ListView

from .models import Team


class TeamListView(ListView):
    model = Team
