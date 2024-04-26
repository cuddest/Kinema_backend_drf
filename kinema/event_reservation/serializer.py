from .models import event_reservation
from rest_framework import serializers


class event_reservation_serializer(serializers.ModelSerializer):
    class Meta:
        model = event_reservation
        fields = "__all__"
