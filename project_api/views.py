import requests
from datetime import datetime, timedelta
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from django.contrib.auth.models import User
from .models import Message, UserToken
import jwt
from dotenv import load_dotenv
import os
from django.contrib.auth import login, authenticate
from project_factory.settings.base import TELEGRAM_TOKEN

# from rest_framework.permissions /import AllowAny

from .serializers import (
    SignUpSerializer,
    MessageSerializer,
    UserTokenSerializer,
    UserTelegramIDSerializer,
    LoginSerializer
)
from rest_framework import generics

# Create your views here.


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(data=user_data, status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            response = {"message": "Login successful"}
            login(request, user)
            return Response(data=response)

        else:
            return Response(
                data={
                    "message": "Invalid username or password",
                    "username": username,
                    "password": password,
                }
            )


def send_message_to_telegram_bot(token, chat_id, message):
    base_url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    response = requests.post(base_url, json=params)
    return response.json()


class MessageView(generics.ListCreateAPIView):
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        # Return messages only for the currently authenticated user
        return Message.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        load_dotenv()
        message = serializer.save()

        # Send the message to Telegram bot
        user_token = UserToken.objects.get(user=self.request.user)
        if user_token.telegram_token and user_token.telegram_id:
            message_content = f"{self.request.user.username}, Я получил от тебя сообщение:\n{message.content}"
            send_message_to_telegram_bot(
                TELEGRAM_TOKEN,
                user_token.telegram_id,
                message_content,
            )

        return message


class UserTokenCreateView(generics.ListCreateAPIView):
    
    serializer_class = UserTokenSerializer

    def get_queryset(self):
        # Return messages only for the currently authenticated user
        return UserToken.objects.filter(user=self.request.user)

    def post(self, request):
        token = jwt.encode(
            {
                "user": self.request.user,
                "exp": datetime.utcnow() + timedelta(minutes=30),
            },
            key="secret_telegram_token",
        )

        user_token, created = UserToken.objects.get_or_create(
            user=request.user)

        user_token.telegram_token = token
        user_token.save()

        return Response({"telegram_token": token}, status=status.HTTP_201_CREATED)


class AddUserTelegramIDView(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = UserToken.objects.all()
    serializer_class = UserTelegramIDSerializer

    def get_object(self):
        # Return the UserToken instance for the current user
        return self.queryset.get(telegram_token=self.request.data.get("telegram_token"))
