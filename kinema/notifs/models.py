from django.db import models


class Notification(models.Model):
    user = models.ForeignKey("cinephile.User", on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"User:{self.user} / Type:{self.type}"
