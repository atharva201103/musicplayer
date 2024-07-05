# player/forms.py
from django import forms
from .models import Music, Playlist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'file', 'category']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = forms.Select(choices=self.fields['category'].widget.choices)

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'musics']
        widgets = {
            'musics': forms.CheckboxSelectMultiple(),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AddMusicToPlaylistForm(forms.Form):
    playlist = forms.ModelChoiceField(queryset=Playlist.objects.all(), empty_label="Select Playlist")
    music = forms.ModelChoiceField(queryset=Music.objects.all(), empty_label="Select Music")