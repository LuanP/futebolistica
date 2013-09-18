# -*- coding: utf-8 -*-

from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=200)


class Judge(models.Model):
    name = models.CharField(max_length=200)


class Game(models.Model):
    stadium = models.ForeignKey('Stadium')
    judge = models.ForeignKey('Judge')
    date = models.DateField()
    team_home = models.ForeignKey('teams.Team', related_name=u'team_one')
    team_away = models.ForeignKey('teams.Team', related_name=u'team_two')
    team_home_score = models.PositiveSmallIntegerField()
    team_away_score = models.PositiveSmallIntegerField()
    game_round = models.ForeignKey('leagues.Round')
