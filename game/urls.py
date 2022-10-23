from django.urls import path

from game import views

app_name = "word_game"

urlpatterns = [
    path("", views.show_home_page, name="home_page"),
    path("enter-name/<slug:name>/", views.show_name_input, name="enter_name"),
    path("game-play/<slug:name>/", views.game_play, name="game_play"),
    path("room/", views.show_room_init, name="choose_room"),
]
