from rest_framework import serializers
from .models import Showtime
from movies.serializers import MovieSerializer
from cinema.serializer import cinemaSerializer
from movies.models import Movie


class Movie_Showtime_Serializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    cinema = cinemaSerializer(read_only=True)

    class Meta:
        model = Showtime
        fields = "__all__"
