from django.views.generic import TemplateView

from leagues.models import League
from teams.models import Team


class HomeView(TemplateView):
    template_name = 'index.html'
