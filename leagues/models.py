# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify


class League(models.Model):
    name = models.CharField(max_length=200)
    period_start = models.DateField()
    period_end = models.DateField()
    round_numbers = models.PositiveSmallIntegerField()
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(League, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Round(models.Model):
    league = models.ForeignKey('League')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('league', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Round, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'{} - {}'.format(self.league, self.name)
