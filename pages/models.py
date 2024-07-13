from django.db import models
from games.models import Game
from datetime import datetime

class GameAd(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    date_add = models.DateTimeField(null=False, default=datetime.now())

    def __str__(self):
        return self.game.name
