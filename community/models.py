from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from games.models import Game

class Community(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Community | {self.game.name}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add = models.DateTimeField(null=False, default=datetime.now())
    content = models.TextField(null=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community_comments")

    def __str__(self):
        return self.user.username