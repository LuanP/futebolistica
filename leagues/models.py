# -*- coding: utf-8 -*-

from django.db import models


class League(models.Model):
    name = models.CharField(max_length=200)
    period_start = models.DateField()
    period_end = models.DateField()


class Round(models.Model):
    games = models.ManyToManyField('games.Game')
    league = models.ForeignKey('League')

    class Meta:
        unique_together = ('games', 'league')
