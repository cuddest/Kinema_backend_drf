from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    Release_Date = models.DateField()
    Genre = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    ProductionCompanies = models.CharField(max_length=100)
    Movie_Cast = models.CharField(default=list, max_length=1000)
    country = models.CharField(max_length=100)
    Description = models.TextField()
    Category = models.CharField(max_length=100)
    Poster = models.URLField(blank=True, null=True)
    Release_Date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


# Create your models here.
