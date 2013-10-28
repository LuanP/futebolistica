# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse


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
    long_slug = models.TextField(null=True, blank=True)

    def __unicode__(self):
        score_1 = self.team_home_score
        score_2 = self.team_home_score
        return u'{} {} x {} {}'.format(
            self.team_home.abbr, score_1 if score_1 else '',
            score_2 if score_2 else '', self.team_away.abbr,
        )
    def save(self, *args, **kwargs):
        self.long_slug = u'{}/{}/{}-vs-{}'.format(
            self.game_round.league.slug,
            self.game_round.slug,
            self.team_home.abbr,
            self.team_away.abbr
        )
        super(Game, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('games:detail', args=(self.long_slug, ))
