from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from accounts.models import CustomUser


class MyCustomRegistrationSerializer(RegisterSerializer):
    CHOICES = (
        ("W", "Warehouse attendant"),
        ("R", "Retailer"),
    )
    role = serializers.ChoiceField(choices=CHOICES)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["role"] = self.validated_data.get("role", "")
        return data_dict


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
            "role",
        )
