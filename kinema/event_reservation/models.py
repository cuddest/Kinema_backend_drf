from django.db import models


class event_reservation(models.Model):
    user = models.ForeignKey("cinephile.User", on_delete=models.CASCADE)
    event = models.ForeignKey(
        "event_showtime.Showtime_events", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.event


# Create your models here.
