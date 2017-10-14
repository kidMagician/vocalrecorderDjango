from rest_framework import serializers
from .models import CustomUser


class CUserSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):

        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        user = CustomUser.objects.get(email = validated_data.email)
        user.set_password(validated_data.password1)