# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import League, Round


class RoundInline(admin.TabularInline):
    model = Round


class LeagueAdmin(admin.ModelAdmin):
    inlines = [RoundInline, ]


class RoundAdmin(admin.ModelAdmin):
    pass


admin.site.register(League, LeagueAdmin)
admin.site.register(Round, RoundAdmin)
