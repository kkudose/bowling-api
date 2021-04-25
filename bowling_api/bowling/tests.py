from django.test import TestCase

from bowling_api.bowling.models import Roll, Game, Player


class BowlingTest(TestCase):
    def setUp(self):
        self.player = Player.objects.create(name="Zesty Zebra")
        self.game = Game.objects.create(player=self.player)

    def roll(self, num_rolls=1, *, num_pins_down):
        for _ in range(num_rolls):
            Roll.objects.create(game=self.game, num_pins_down=num_pins_down)

    def roll_spare(self):
        self.roll(num_rolls=2, num_pins_down=5)

    def roll_strike(self):
        self.roll(num_rolls=1, num_pins_down=10)

    def test_all_gutters(self):
        self.roll(num_pins_down=0, num_rolls=20)
        rolls = self.game.rolls

        self.assertEqual(rolls.count(), 20)

        for roll in rolls.all():
            self.assertEqual(roll.num_pins_down, 0)

        self.assertEqual(self.game.total_score, 0)

    def test_all_spares(self):
        self.roll(num_pins_down=5, num_rolls=21)
        rolls = self.game.rolls

        self.assertEqual(rolls.count(), 21)

        for roll in rolls.all():
            self.assertEqual(roll.num_pins_down, 5)

        self.assertEqual(self.game.total_score, 150)

    def test_all_strikes(self):
        self.roll(num_pins_down=10, num_rolls=10 + 2)
        rolls = self.game.rolls

        self.assertEqual(rolls.count(), 12)

        for roll in rolls.all():
            self.assertEqual(roll.num_pins_down, 10)

        self.assertEqual(self.game.total_score, 300)

    def test_spare(self):
        self.roll_spare()
        self.roll(num_pins_down=3)

        self.assertEquals(self.game.rolls.count(), 3)

        frame_one_score = self.game.frame_scores[0]
        self.assertEqual(frame_one_score, 10 + 3)

    def test_strike(self):
        self.roll_strike()
        self.roll(num_pins_down=3, num_rolls=2)

        self.assertEquals(self.game.rolls.count(), 3)

        frame_one_score = self.game.frame_scores[0]
        self.assertEqual(frame_one_score, 10 + 3 + 3)
        frame_two_score = self.game.frame_scores[1]
        self.assertEqual(frame_two_score, frame_one_score + 3 + 3)
