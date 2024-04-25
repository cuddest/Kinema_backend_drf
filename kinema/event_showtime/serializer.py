from rest_framework import serializers
from .models import Showtime_events


class Event_Showtime_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime_events
        fields = "__all__"

