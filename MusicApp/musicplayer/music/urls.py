# player/urls.py
from django.urls import path
from .views import music_list, playlist_list, add_music, add_playlist,index,register,add_music_to_playlist
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('musics/', music_list, name='music_list'),
    path('playlists/', playlist_list, name='playlist_list'),
    path('add_music/', add_music, name='add_music'),
    path('add_playlist/', add_playlist, name='add_playlist'),
    path('',index,name='index'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('add_music_to_playlist/', add_music_to_playlist, name='add_music_to_playlist'),
]
