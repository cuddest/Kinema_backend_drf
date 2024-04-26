from django.db import models


class event_reservation(models.Model):
    user = models.ForeignKey("cinephile.User", on_delete=models.CASCADE)
    event = models.ForeignKey("events.event", on_delete=models.CASCADE)
    qr_code = models.URLField(max_length=200)

    def __str__(self):
        return self.event


# Create your models here.
