# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from PIL import Image

from futebolistica.settings import MEDIA_URL


class Team(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=3)
    flag = models.ImageField(upload_to='flags')
    players = models.ManyToManyField('Player', through='TeamPlayer')
    slug = models.SlugField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams:detail', args=[self.slug, ])

    def get_flag_url(self):
        return u'{}{}'.format(MEDIA_URL, self.flag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        image = Image.open(self.flag)
        (width, height) = image.size
        image = image.resize((25, 23), Image.ANTIALIAS)
        super(Team, self).save(*args, **kwargs)
        image.save(self.flag.path)


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Player(models.Model):
    name = models.CharField(max_length=200)
    position = models.ForeignKey('Position')

    def __unicode__(self):
        return self.name


class TeamPlayer(models.Model):
    team = models.ForeignKey('Team')
    shirt_number = models.PositiveSmallIntegerField()
    player = models.ForeignKey('Player')
    league = models.ForeignKey('leagues.League')

    class Meta:
        ordering = ('league', 'team', 'player__name')
        unique_together = (
            ('league', 'player'),
            ('team', 'shirt_number', 'league'),
        )

    def __unicode__(self):
        return u'{} - {} ({})'.format(self.player, self.team, self.league)
