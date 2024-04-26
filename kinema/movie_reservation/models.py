from django.db import models


class movie_reservation(models.Model):
    user = models.ForeignKey("cinephile.User", on_delete=models.CASCADE)
    showtime = models.ForeignKey("movie_showtime.ShowTime", on_delete=models.CASCADE)
    qr_code = models.URLField(max_length=200)

    def __str__(self):
        return self.movie


# Create your models here.
