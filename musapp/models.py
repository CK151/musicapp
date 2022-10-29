from datetime import date, datetime
from email import contentmanager
from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    fistname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    age = models.IntegerField()



#Song class
class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT)
    title = models.CharField(max_length=60)
    date_released = models.DateField(default=datetime.today)
    likes = models.BooleanField()
    artiste_id = models.IntegerField()


#lyric class

class Lyric(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT)
    Song = models.ForeignKey(Song, on_delete=models.PROTECT)
    content = models.TextField()
    song_id = models.IntegerField()
