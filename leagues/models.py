# -*- coding: utf-8 -*-

from django.db import models


class League(models.Model):
    name = models.CharField(max_length=200)
    period_start = models.DateField()
    period_end = models.DateField()
    round_numbers = models.PositiveSmallIntegerField()


class Round(models.Model):
    league = models.ForeignKey('League')
    name = models.CharField(max_length=200)
