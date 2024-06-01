from django.db import models


class Showtime_events(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey("events.event", on_delete=models.CASCADE)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    price = models.IntegerField()
    stock = models.IntegerField()
    cinema = models.ForeignKey("cinema.cinema", on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title

