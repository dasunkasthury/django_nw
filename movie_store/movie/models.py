from django.db import models


class Director(models.Model):
    director_name = models.CharField(max_length=250)
    age = models.IntegerField()
    picture = models.CharField(max_length=250)

    def __str__(self):
        return self.director_name


class Genres(models.Model):
    genres_category = models.CharField(max_length=250)

    def __str__(self):
        return self.genres_category


class Movies(models.Model):

    movie_name = models.CharField(max_length=250)
    year = models.IntegerField()
    duration = models.CharField(max_length=250)
    ratings = models.IntegerField()
    language = models.CharField(max_length=250)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres)
    poster = models.CharField(max_length=1000)

    def __str__(self):
        return self.movie_name
