
from django.shortcuts import render, redirect
from .models import Music, Playlist, Category
from .form import MusicForm, PlaylistForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .form import AddMusicToPlaylistForm

@login_required
def music_list(request):
    musics = Music.objects.all()
    return render(request, 'music_list.html', {'musics': musics})

@login_required
def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist_list.html', {'playlists': playlists})

@login_required
def add_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:
        form = MusicForm()
    return render(request, 'add_music.html', {'form': form})

@login_required
def add_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlist_list.html')
    else:
        form = PlaylistForm()
    return render(request, 'add_playlist.html', {'form': form})

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('music_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_music_to_playlist(request):
    if request.method == 'POST':
        form = AddMusicToPlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.cleaned_data['playlist']
            music = form.cleaned_data['music']
            playlist.musics.add(music)  # Add music to playlist
            return redirect('playlist_list')  # Redirect to playlist list page after adding music
    else:
        form = AddMusicToPlaylistForm()
    return render(request, 'add_music_to_playlist.html', {'form': form})