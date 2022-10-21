from django.urls import path
from game import views

app_name = "word_game"

urlpatterns = [
    path("", views.show_home_page, name="home_page"),
    path("room/", views.show_room, name="game"),
    path("game-play/",views.game_play, name="game_play"),
]
