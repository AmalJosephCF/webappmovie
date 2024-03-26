from django.contrib.auth.models import User
from django.db import models

from movieapp.models import Movie


class MovieFavourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')