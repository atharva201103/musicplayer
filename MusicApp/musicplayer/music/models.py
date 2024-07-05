# player/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to='music/')
    category = models.CharField(max_length=50, choices=[
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('hiphop', 'Hip Hop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        # Add more categories as needed
    ])
    audio_file = models.FileField(upload_to='music/',default='music/placeholder.mp3') 

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    musics = models.ManyToManyField(Music,related_name='playlists')

    def __str__(self):
        return self.name
