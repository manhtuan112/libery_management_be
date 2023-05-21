
from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=2, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs["email"]).exists()
        username_exitsts = User.objects.filter(
            username=attrs["username"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")
        if username_exitsts:
            raise ValidationError("Username has already been used")

        return super().validate(attrs)




class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=2, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']