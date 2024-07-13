from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=35, null=False)
    description = models.TextField(null=False)
    cover = models.ImageField(upload_to="GameImages/%Y/%m/%d/", null=False)
    game_file = models.FileField(upload_to="Games/%Y/%m/%d/", null=False)
    rate = models.IntegerField(null=False)
    date_add = models.DateTimeField(null=False, default=datetime.now())

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["-date_add"]

class InfoDownload(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_info_download")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.user_id.username}_{self.date_add}"
    

class GameImage(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_images")
    images = models.ImageField(upload_to="GameImages/%Y/%m/%d/", null=False)
    date_add = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.game_id.name
    
    class Meta:
        ordering = ["-date_add"]