from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)
    ticket_sales = models.FloatField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.name


