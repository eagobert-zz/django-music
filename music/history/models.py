from django.db import models

# Create your models here.
class Artist(models.Model):
    """ Model represents a song's artist """
    artist_name = models.CharField(max_length=30)
    year_est = models.CharField(max_length=4)

    def __str__(self):
        return self.artist_name

class Genre(models.Model):
    """ Model represents an album's genre """
    genre_name = models.CharField(max_length=30)

    def __str__(self):
        return self.genre_name

class Album(models.Model):
    """ Model represents an artist's album """
    title = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    songs = models.ManyToManyField('Song', through='AlbumSongs')

    def __str__(self):
        return self.title
        
class Song(models.Model):
    """ Model represents an artist's song """
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    song_length = models.IntegerField(default=0)
    release_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

class AlbumSongs(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    song = models.ForeignKey(Song, on_delete= models.CASCADE)