# -*- coding: utf-8 -*-

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=3)
    # flag = models.ImageField(upload_to='flags')
    players = models.ManyToManyField('Player', through='TeamPlayer')


class Position(models.Model):
    title = models.CharField(max_length=100)


class Player(models.Model):
    name = models.CharField(max_length=200)
    position = models.ForeignKey('Position')


class TeamPlayer(models.Model):
    team = models.ForeignKey('Team')
    shirt_number = models.PositiveSmallIntegerField()
    player = models.ForeignKey('Player')
    league = models.ForeignKey('leagues.League')

    class Meta:
        unique_together = ('league', 'player')
