from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import test_token, UserViewSet, DiscordUserCreate

urlpatterns = [
    path('test_token/', test_token),
    path('create/', DiscordUserCreate.as_view())
]
