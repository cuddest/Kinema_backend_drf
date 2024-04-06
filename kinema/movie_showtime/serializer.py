from rest_framework import serializers
from .models import Showtime


class Movie_Showtime_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = "__all__"

