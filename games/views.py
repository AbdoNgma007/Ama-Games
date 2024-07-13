from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.core.paginator import Paginator
from games.models import Game, GameImage,InfoDownload
from community.models import Community

def games(request):
    all_games = Game.objects.all()
    paginations = Paginator(all_games, 6)
    page = request.GET.get("page")
    all_games = paginations.get_page(page)
    context = {
        "games": all_games
    }
    return render( request, "games/games.html", context )

def game(request, gm_id):
    _game = get_object_or_404(Game, pk=gm_id)
    _comm = Community.objects.filter(game=_game)
    context = {
        "game": _game,
        "images": GameImage.objects.filter(game_id=gm_id),
        "comm": _comm
    }
    return render( request, "games/game.html", context )

def gameDownload(request, target_game_id):
    # variables
    game = Game.objects.get(id=target_game_id)
    # save to database
    if "btndownload" in request.GET:
        info = InfoDownload.objects.create(
            user_id=request.user, game_id=game
        )
        info.save()
    # download
    response = FileResponse()
    response['Content-Disposition'] = 'attachment; filename=%s' % game.game_file.name 
    return response

def gameSearch(request):
    target_name = None
    games = []
    if "target_name" in request.GET:
        target_name = request.GET["target_name"]
        games = Game.objects.filter(name__icontains=target_name)
    context = {
        "games": games
    }
    return render( request, "games/game_results.html", context )
