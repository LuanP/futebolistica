# -*- coding: utf-8 -*-

from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=200)


class Judge(models.Model):
    name = models.CharField(max_length=200)


class GameTeam(models.Model):
    game = models.ForeignKey('Game')
    team = models.ForeignKey('teams.Team')
    score = models.SmallIntegerField()


class Game(models.Model):
    stadium = models.ForeignKey('Stadium')
    judge = models.ForeignKey('Judge')
    date = models.DateField()
    team_1 = models.ForeignKey('teams.Team')
    team_2 = models.ForeignKey('teams.Team')
