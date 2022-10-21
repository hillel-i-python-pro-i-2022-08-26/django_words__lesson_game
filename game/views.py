from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from game.forms import UserName, InputWord
from game.models import User, Word


def show_home_page(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "base.html",
    )


def show_room(request: HttpRequest):
    if request.method == "POST":
        form = UserName(request.POST)
        if form.is_valid():
            form.save()
            return redirect("word_game:game")
    else:
        form = UserName()
    return render(
        request,
        "game/game.html",
        {
            "title": "Add User",
            "form": form,
        },
    )


def game_play(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = InputWord(request.POST)
        if form.is_valid():
            form.save()
            return redirect("word_game:game_play")
    else:
        form = InputWord()
    return render(
        request,
        "game/gameplay.html",
        {
            "title": "Playroom",
            "form": form,
        },
    )

