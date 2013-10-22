# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Team, Position, Player, TeamPlayer


class TeamAdmin(admin.ModelAdmin):
    pass


class PositionAdmin(admin.ModelAdmin):
    pass


class TeamPlayerInline(admin.TabularInline):
    model = TeamPlayer


class PlayerAdmin(admin.ModelAdmin):
    inlines = [TeamPlayerInline, ]


class TeamPlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(TeamPlayer, TeamPlayerAdmin)
