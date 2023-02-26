from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, MovieLike


# Create your models here.
def profile_image_path(instance, filename):
    return f'profile/{instance.username}/{filename}'

class User(AbstractUser):
    pass
    followings = models.ManyToManyField('self', symmetrical = False, related_name = 'followers')
    movies = models.ManyToManyField(Movie, through=MovieLike, related_name='like_user')
    profile_image = models.ImageField(default='/profile/default.png', blank=True, upload_to=profile_image_path)