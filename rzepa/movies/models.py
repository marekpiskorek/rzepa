from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128, unique=True, db_index=True)
    actors = models.CharField(max_length=256, blank=True, default="")
    awards = models.CharField(max_length=256, blank=True, default="")
    box_office = models.CharField(max_length=32, blank=True, default="")
    country = models.CharField(max_length=32, blank=True, default="")
    dvd = models.CharField(max_length=32, blank=True, default="")
    director = models.CharField(max_length=32, blank=True, default="")
    genre = models.CharField(max_length=32, blank=True, default="")
    language = models.CharField(max_length=64, blank=True, default="")
    metascore = models.CharField(max_length=16, blank=True, default="")
    plot = models.TextField(blank=True, default="")
    poster = models.CharField(max_length=256, blank=True, default="")
    production = models.CharField(max_length=64, blank=True, default="")
    rated = models.CharField(max_length=16, blank=True, default="")
    released = models.CharField(max_length=32, blank=True, default="")
    runtime = models.CharField(max_length=16, blank=True, default="")
    type = models.CharField(max_length=16, blank=True, default="")
    website = models.CharField(max_length=128, blank=True, default="")
    writer = models.CharField(max_length=32, blank=True, default="")
    year = models.CharField(max_length=16, blank=True, default="")
    imdbID = models.CharField(max_length=16, blank=True, default="")
    imdbRating = models.CharField(max_length=16, blank=True, default="")
    imdbVotes = models.CharField(max_length=16, blank=True, default="")


class Rating(models.Model):
    source = models.CharField(max_length=64)
    value = models.CharField(max_length=16)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="ratings")
