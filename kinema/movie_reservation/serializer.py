from .models import movie_reservation
from rest_framework import serializers


class movie_reservation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = movie_reservation
        fields = "__all__"
