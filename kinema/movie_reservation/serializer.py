from .models import movie_reservation
from rest_framework import serializers
from movie_showtime.models import Showtime
from movies.serializers import MovieSerializer
from movie_showtime.serializer import Movie_Showtime_Serializer


class movie_reservation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = movie_reservation
        fields = "__all__"


class MovieReservationWithShowtimeSerializer(serializers.ModelSerializer):
    showtime = Movie_Showtime_Serializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = movie_reservation
        fields = "__all__"  


class ShowtimeWithMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Showtime
        fields = "__all__"
