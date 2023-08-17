from django.contrib import admin
from django.urls import include, path

from .views import (
    SignUpView,
    LoginView,
    MessageView,
    UserTokenCreateView,
    AddUserTelegramIDView,
)

urlpatterns = [
    path("register/", SignUpView.as_view(), name="user-registration"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("message/", MessageView.as_view(), name="user-message"),
    path("create-token/", UserTokenCreateView.as_view(), name="token-creation"),
    path("add-telegram-id/", AddUserTelegramIDView.as_view(), name="add-telegram-id"),
]
