from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect

from game.forms import UserName, InputWord, RoomForm, ContinueForm
from game.models import Room, Word


def show_name_input(request: HttpRequest, name: Room.room_name) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        form = UserName(request.POST)
        if form.is_valid():
            form.save()
            return redirect("word_game:enter_name", name=name)
    else:
        form = UserName()
    return render(
        request,
        "game/register_players.html",
        {
            "title": "Add User",
            "form": form,
            "name": name,
        },
    )


def game_play(request: HttpRequest, name: Room.room_name) -> HttpResponse | HttpResponseRedirect:
    room = Room.objects.get(room_name=name)
    if request.method == "POST":
        form = InputWord(request.POST)
        if form.is_valid():
            word = Word(word=form.input_word, user_words_id=room.room_name)
            room.word_set.all()
            word.save()
            messages.info(request, 'Word is accepted!')
            return redirect("word_game:game_play", name=name)
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


def show_room_init(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            name = Room.objects.get(room_name=form.cleaned_data['room_name'])
            return redirect("word_game:enter_name", name=name.room_name)
    else:
        form = RoomForm()
    return render(
        request,
        "game/choose_room.html",
        {
            "title": "Choose Room",
            "form": form,
        },
    )


def show_home_page(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        form = ContinueForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['room_name']
            return redirect("word_game:game_play", name=name)
    else:
        form = ContinueForm()
    return render(
        request,
        "base.html",
        {
            "form": form,
        },
    )
