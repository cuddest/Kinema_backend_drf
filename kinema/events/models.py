from django.db import models


class event(models.Model):
    id = models.IntegerField(primary_key=True)
    theme = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    guests = models.CharField(blank=True, max_length=100)
    private = models.BooleanField(default=False)
    Description = models.TextField()
    Poster = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# Create your models here.
