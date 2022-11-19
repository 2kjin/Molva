from django.db import models
from django.conf import settings
from movies.models import Movie, Review

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="like_reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="posts")

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField()

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")


class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)

    post = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
