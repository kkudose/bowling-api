from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Player(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(blank=True, max_length=127)

    def __str__(self):
        name_postfix = f", {self.name}" if self.name else ""
        return f"Player {self.id}{name_postfix}"


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="games")

    current_roll_num = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(21)],
    )

    @property
    def total_score(self):
        frame_scores = self.frame_scores
        return frame_scores[-1] if len(frame_scores) > 0 else 0

    @property
    def frame_scores(self):
        scores = []
        rolls = self.rolls.order_by("num_in_game").values_list(
            "num_pins_down", flat=True
        )

        num_roll = 0
        rolls_max_index = self.current_roll_num - 1
        while num_roll + 1 < rolls_max_index:
            first_roll = rolls[num_roll]
            second_roll = rolls[num_roll + 1]
            is_strike = first_roll == 10
            is_spare = first_roll + second_roll == 10
            prev_frame_score = scores[-1] if len(scores) else 0
            frame_score = prev_frame_score
            if len(scores) == 9:
                third_roll = (
                    rolls[num_roll + 2] if num_roll + 2 < rolls_max_index else 0
                )
                scores.append(prev_frame_score + first_roll + second_roll + third_roll)
                break

            if is_strike:
                if num_roll + 2 > rolls_max_index:
                    break
                next_two_rolls = second_roll + rolls[num_roll + 2]
                frame_score += 10 + next_two_rolls
                num_roll += 1
            elif is_spare:
                if num_roll + 2 > rolls_max_index:
                    break
                next_roll = rolls[num_roll + 2]
                frame_score += 10 + next_roll
                num_roll += 2
            else:
                frame_score += first_roll + second_roll
                num_roll += 2

            scores.append(frame_score)

        return scores

    def __str__(self):
        return f"Game {self.id} with {self.player}"


class Roll(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    num_pins_down = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(10)]
    )
    num_in_game = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(21)]
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="rolls")
