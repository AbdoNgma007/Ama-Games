from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Comment, Community


def communities(request):
    _communities = Community.objects.all()
    paginations = Paginator(_communities, 3)
    page = request.GET.get("page")
    _communities = paginations.get_page(page)
    context = {
        "communities": _communities
    }
    return render(request, "community/community.html", context)

def community(request, com_id):
    _community = get_object_or_404(Community, pk=com_id)
    _comments = Comment.objects.filter(community=_community)
    context = {
        "community":_community,
        "comments": _comments,
    }
    return render(request, "community/community_game.html", context)

def createComment(request, com_id):
    community = get_object_or_404(Community, pk=com_id)
    if "contentcomment" in request.GET:
        content = request.GET["contentcomment"]
        new_comment = Comment.objects.create(
            user=request.user, 
            community=community,
            content=content,
        )
        new_comment.save()
    return redirect("community", com_id)