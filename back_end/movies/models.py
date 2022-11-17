from django.db import models

# Create your models here.

class Genre(models.Model):
    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=50)

class Actor(models.Model):
    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=50)

class Director(models.Model):
    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    actors = models.ManyToManyField(Actor, related_name='movie_actor')
    directors = models.ManyToManyField(Director, related_name='movie_director')
    

    id = models.TextField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.title
