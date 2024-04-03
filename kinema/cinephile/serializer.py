from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            "Full_Name",
            "username",
            "email",
            "Phone_Number",
            "Address",
            "Date_of_Birth",
            "Profile_Picture",
            "is_admin",
            "is_customer",
            "is_staff",
            "is_superuser",
            "Fidelity_Points",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
