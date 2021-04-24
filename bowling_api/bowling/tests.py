from django.test import TestCase

from bowling_api.bowling.services import bowling_service


class BowlingTest(TestCase):
    def setUp(self):
        self.player = bowling_service.create_player(name="Zesty Zebra")
        self.game = bowling_service.create_game(player=self.player)

    def roll_pins(self, *, num_pins, num_rolls):
        for _ in range(num_rolls):
            bowling_service.update_game(game_id=self.game.id, roll=num_pins)

    def test_all_gutters(self):
        self.roll_pins(num_pins=0, num_rolls=20)
        frames = self.game.frames

        self.assertEqual(frames.count(), 10)

        for frame in frames.all():
            self.assertEqual(frame.roll_one, 0)
            self.assertEqual(frame.roll_two, 0)

        tenth_frame = frames.get(num_in_game=10)
        self.assertIsNone(tenth_frame.roll_three)

        self.assertEqual(self.game.score, 300)  # TODO
