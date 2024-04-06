from django.db import models


class Showtime(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    price = models.IntegerField()
    stock = models.IntegerField()
    cinema = models.ForeignKey("cinema.cinema", on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title
