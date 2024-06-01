from django.db import models


class item(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    description = models.TextField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    points_price = models.IntegerField()
    stock = models.IntegerField()
    imgurl = models.URLField(blank=True, null=True)
    merch_type = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name
