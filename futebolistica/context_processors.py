from teams.models import Team


def get_teams(request):
    return dict(teams=Team.objects.iterator())
