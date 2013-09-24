from django.views.generic import TemplateView

from leagues.models import League
from teams.models import Team


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['leagues'] = League.objects.all()
        context['teams'] = Team.objects.all()
        return context
