from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, UserToken


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        

class UserTelegramIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = ["telegram_id", "telegram_token"]

    def update(self, instance, validated_data):
        instance.telegram_id = validated_data.get("telegram_id", instance.telegram_id)
        instance.save()
        return instance


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "first_name"]

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        first_name = attrs.get("first_name")

        if not username or not password:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg)

        if not first_name:
            msg = "First name must be provided"
            raise serializers.ValidationError(msg)

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
