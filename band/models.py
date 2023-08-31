from django.db import models

# Create your models here.
# The MusicItem model is used to create a database table with the following fields, Title of the song, The release date oft he song and Whether the song is released or not.
class MusicItem(models.Model):
    title = models.CharField(max_length=20)
    release_date = models.DateField()
    released = models.BooleanField(default=False)

# The TourItem model is used to craete a database table with the following fields,Title of the tour, The tour date, and whether tickets are available or not.
class TourItem(models.Model):
    title = models.CharField(max_length=20)
    tour_date = models.DateField()
    tickets = models.BooleanField(default=False)
