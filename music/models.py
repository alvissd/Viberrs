from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

class Album(models.Model):
    album_title = models.CharField(max_length=200)
    album_description = models.CharField(max_length=200)
    album_artist = models.CharField(max_length=200)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title+" by "+self.album_artist
    
class Song(models.Model):
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=10,null=True)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.song_title+" - "+str(self.album_id.album_artist)
# Create your models here.
