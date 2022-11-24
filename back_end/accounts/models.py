from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
def profile_image_path(instance, filename):
    return f'profile/{instance.username}/{filename}'

class User(AbstractUser):
    pass
    followings = models.ManyToManyField('self', symmetrical = False, related_name = 'followers')
    profile_image = models.ImageField(default='/profile/default.png', blank=True, upload_to=profile_image_path)