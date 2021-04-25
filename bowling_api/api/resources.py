from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from django.utils import timezone

from bowling_api.bowling.models import Game, Player, Roll


# WARNING: authorization = Authorization() is not appropriate for prod
# This demo has no need for auth as it is only ever run locally


class PlayerResource(ModelResource):
    created_at = fields.DateTimeField(readonly=True, default=timezone.now())
    updated_at = fields.DateTimeField(readonly=True, default=timezone.now())

    class Meta:
        queryset = Player.objects.all()
        authorization = Authorization()
        always_return_data = True


class GameResource(ModelResource):
    created_at = fields.DateTimeField(readonly=True, default=timezone.now())
    updated_at = fields.DateTimeField(readonly=True, default=timezone.now())

    player = fields.ForeignKey(PlayerResource, "player")

    num_in_game = fields.IntegerField(readonly=True)
    total_score = fields.IntegerField(attribute="total_score", readonly=True)
    frame_scores = fields.ListField(attribute="frame_scores", readonly=True)

    class Meta:
        queryset = Game.objects.all()
        authorization = Authorization()
        always_return_data = True


class RollResource(ModelResource):
    created_at = fields.DateTimeField(readonly=True, default=timezone.now())
    updated_at = fields.DateTimeField(readonly=True, default=timezone.now())

    game = fields.ForeignKey(GameResource, "game")

    class Meta:
        queryset = Roll.objects.all()
        authorization = Authorization()
        always_return_data = True
        allowed_methods = ["get", "post"]
