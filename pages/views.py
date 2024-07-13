from django.shortcuts import render
from games.models import Game
from .models import GameAd
# Create your views here.

def index(request):
    # get games from db
    ads = GameAd.objects.all()
    print('=' * 15)
    print(ads)
    if ads:
        ads = list(ads)[-1]
    context = {
        "games": Game.objects.all()[:6],
        "ads": ads
    }
    return render( request, "pages/index.html", context )