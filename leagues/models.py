# -*- coding: utf-8 -*-

from django.db import models


class League(models.Model):
    name = models.CharField(max_length=200)
    period_start = models.DateField()
    period_end = models.DateField()
    round_numbers = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name


class Round(models.Model):
    league = models.ForeignKey('League')
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('league', )

    def __unicode__(self):
        return u'{} - {}'.format(self.league, self.name)
