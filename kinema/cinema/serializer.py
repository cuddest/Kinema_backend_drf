from rest_framework import serializers
from .models import cinema


class cinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cinema
        fields = "__all__"
