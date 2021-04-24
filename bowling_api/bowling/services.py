from django.core.exceptions import ValidationError

from bowling_api.bowling.models import Game, Frame, Player


class BowlingService:
    def create_player(self, name):
        player = Player.objects.create(name=name)
        return player

    def create_game(self, *, player):
        game = Game.objects.create(player=player)
        Frame.objects.create(game=game, num_in_game=1)

        return game

    def update_game(self, *, game_id, roll):
        game = Game.objects.get(id=game_id)

        if roll < 0 or roll > 10:
            raise ValidationError("Must knock down between zero and ten pins")

        frame_count = game.frames.count()
        frame = game.frames.get(num_in_game=frame_count)

        is_third_roll_allowed = frame_count == 10 and (
            frame.is_strike or frame.is_strike
        )

        if frame.roll_one is None:
            frame.roll_one = roll
        elif frame.roll_two is None:
            frame.roll_two = roll
        elif is_third_roll_allowed:
            frame.roll_three = roll

        frame.save()

        if frame_count != 10 and (frame.is_strike or frame.roll_two is not None):
            Frame.objects.create(game=game, num_in_game=frame_count + 1)

        return game


bowling_service = BowlingService()
