from django.urls import path
from . import views
urlpatterns = [
    path('', views.games, name="games"),
    path('<int:gm_id>', views.game, name="game"),
    path('download/<int:target_game_id>', views.gameDownload, name="gamedownload"),
    path('search', views.gameSearch, name="searchgame"),
]