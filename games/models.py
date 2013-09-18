# -*- coding: utf-8 -*-

from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Judge(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    stadium = models.ForeignKey('Stadium', null=True, blank=True)
    judge = models.ForeignKey('Judge', null=True, blank=True)
    date = models.DateTimeField()
    team_home = models.ForeignKey('teams.Team', related_name=u'team_one')
    team_away = models.ForeignKey('teams.Team', related_name=u'team_two')
    team_home_score = models.PositiveSmallIntegerField(null=True, blank=True)
    team_away_score = models.PositiveSmallIntegerField(null=True, blank=True)
    game_round = models.ForeignKey('leagues.Round')

    def __unicode__(self):
        return u'{} {} x {} {}'.format(
            self.team_home.abbr, self.team_home_score,
            self.team_away_score, self.team_away.abbr,
        )
