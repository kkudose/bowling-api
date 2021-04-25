from django.contrib import admin

from bowling_api.bowling.models import Game, Player, Roll


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "name")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "player")


@admin.register(Roll)
class RollAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "num_pins_down", "num_in_game", "game")
