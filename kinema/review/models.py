from django.db import models


class review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("cinephile.User", on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
