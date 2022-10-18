from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from game.forms import UserName, InputWord


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
            messages.success(request, "User has been created successfully.")
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
