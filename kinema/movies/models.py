from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Movie(models.Model):
    title = models.CharField(max_length=10000)
    Release_Date = models.DateField()
    Genre = models.CharField(max_length=10000)
    Language = models.CharField(max_length=10000)
    Duration = models.CharField(max_length=10000)
    ProductionCompanies = models.CharField(max_length=10000)
    Movie_Cast = models.CharField(default=list, max_length=10000)
    country = models.CharField(max_length=100000)
    Description = models.TextField()
    Category = models.CharField(max_length=100000)
    Poster = models.URLField(blank=True, null=True)
    Release_Date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


# Create your models here.
