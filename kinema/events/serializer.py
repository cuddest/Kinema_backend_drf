from rest_framework import serializers
from .models import event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = "__all__"


