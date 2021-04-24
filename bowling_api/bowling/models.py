from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Player(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)

    name = models.CharField(blank=True, max_length=127)

    def __str__(self):
        name_postfix = f", {self.name}" if self.name else ""
        return f"Player {self.id}{name_postfix}"


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="games")

    @property
    def score(self):
        return 300  # TODO

    def __str__(self):
        return f"Game {self.id} with {self.player}"


class Frame(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)

    roll_one = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(10)]
    )
    roll_two = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(10)]
    )
    roll_three = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(10)]
    )
    num_in_game = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="frames")

    @property
    def is_strike(self):
        return self.roll_one == 10

    @property
    def is_spare(self):
        return not self.is_strike and self.roll_one + self.roll_two == 10

    def clean(self):
        if self.roll_two is not None and self.roll_one is None:
            raise ValidationError(
                {"roll_two": "Cannot roll second roll before first roll"}
            )

        if self.num_in_game == 10:
            if self.roll_three is not None:
                if self.roll_one is None:
                    raise ValidationError(
                        {"roll_three": "Cannot roll third roll before first roll"}
                    )
                if self.roll_two is None:
                    raise ValidationError(
                        {"roll_three": "Cannot roll third roll before second roll"}
                    )
                if self.roll_one != 10 or self.roll_one + self.roll_two != 10:
                    raise ValidationError(
                        {
                            "roll_three": "Cannot roll third roll without a strike or spare in frame"
                        }
                    )
        else:
            if self.roll_three is not None:
                raise ValidationError(
                    {"roll_three": "Cannot roll third roll in non-tenth frame"}
                )
            if self.roll_one == 10 and self.roll_two is not None:
                raise ValidationError(
                    {"roll_two": "Cannot roll after strike in non-tenth frame"}
                )
            if (self.roll_one is not None and self.roll_two is not None) and (
                self.roll_one + self.roll_two > 10
            ):
                raise ValidationError(
                    {"roll_two": "Cannot knock down than ten pins in non-tenth frame"}
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
