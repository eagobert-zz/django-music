from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=30)
    year_est = models.CharField(max_length=4)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    song_length = models.IntegerField(default=0)
    release_date = models.DateField(auto_now=False, auto_now_add=False)