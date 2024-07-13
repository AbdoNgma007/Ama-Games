from django.contrib import admin
from .models import Game, InfoDownload, GameImage

# Register your models here.
admin.site.register(Game)
admin.site.register(GameImage)
admin.site.register(InfoDownload)