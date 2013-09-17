# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Stadium, Judge, GameTeam, Game


class StadiumAdmin(admin.ModelAdmin):
    pass


class JudgeAdmin(admin.ModelAdmin):
    pass


class GameTeamAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(GameTeam, GameTeamAdmin)
admin.site.register(Game, GameAdmin)
