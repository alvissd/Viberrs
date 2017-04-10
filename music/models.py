from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    album_title = models.CharField(max_length=200)
    album_description = models.CharField(max_length=200)
    album_artist = models.CharField(max_length=200)
    album_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title+" by "+self.album_artist

class Song(models.Model):
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
# Create your models here.
