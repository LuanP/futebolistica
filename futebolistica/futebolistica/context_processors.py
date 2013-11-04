from teams.models import Team
from leagues.models import League


def get_teams(request):
    return dict(teams=Team.objects.all()[:5])

def get_leagues(request):
    return dict(leagues=League.objects.all())
