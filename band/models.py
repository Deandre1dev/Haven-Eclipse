"""
This module is used to create the models for the band application.
"""
from django.db import models

# Create your models here.
# The MusicItem model is used to create a database table with the following fields, Title of the song, The release date oft he song and Whether the song is released or not.
class MusicItem(models.Model):
    """The MusicItem model creates a database table with the following fields for the music object.

    :param title: Creates a field to store the title of the Music.
    :param release_date: Creates a field to store the release date of the Music.
    :param released: Creates a field to store the released information of the Music.
    """
    title = models.CharField(max_length=20)
    release_date = models.DateField()
    released = models.BooleanField(default=False)

# The TourItem model is used to craete a database table with the following fields,Title of the tour, The tour date, and whether tickets are available or not.
class TourItem(models.Model):
    """The TourItem model creates a database table with the following fields for the tour object.

    :param title: Creates a field to store the title of the Tour object.
    :param tour_date: Creates a field to store the tour date of the Tour object.
    :param tickets: Creates a field to store the tickets availability of the tour object.
    """
    title = models.CharField(max_length=20)
    tour_date = models.DateField()
    tickets = models.BooleanField(default=False)
