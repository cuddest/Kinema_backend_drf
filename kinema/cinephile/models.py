from django.db import models
from django.contrib.auth.models import AbstractUser


# User model for the cinema app
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    Full_Name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=15)
    Address = models.TextField()
    Date_of_Birth = models.DateField()
    Profile_Picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True
    )
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    Fidelity_Points = models.FloatField(default=0)
    password = models.CharField(max_length=500)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "Full_Name",
        "Phone_Number",
        "Address",
        "Date_of_Birth",
        "password",
        "email",
    ]

    def __str__(self):
        return self.Full_Name
