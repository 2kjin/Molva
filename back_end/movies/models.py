from django.db import models

# Create your models here.

# class Genre(models.Model):
#     name = models.CharField(max_length=50)

# class Actor(models.Model):
#     name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200, default=None)
    # genres = models.ManyToManyField(Genre)
    # actores = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
