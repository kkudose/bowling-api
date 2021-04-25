from django.core.exceptions import ValidationError

from bowling_api.bowling.models import Roll, Game, Player


class BowlingService:
    def play(self, name):
        player = self.create_player(name=name)
        game = self.create_game(player=player)

        return game

    def create_player(self, name):
        player = Player.objects.create(name=name)
        return player

    def create_game(self, *, player):
        game = Game.objects.create(player=player)
        return game

    def update_game(self, *, game_id, num_pins_down):
        game = Game.objects.get(id=game_id)

        if num_pins_down < 0 or num_pins_down > 10:
            raise ValidationError("Must knock down between zero and ten pins")

        Roll.objects.create(
            game=game, num_pins_down=num_pins_down, num_in_game=game.current_roll_num
        )

        game.current_roll_num += 1
        game.save()

        return game


bowling_service = BowlingService()
