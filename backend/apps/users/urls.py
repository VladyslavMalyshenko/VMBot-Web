from django.urls import path

from .views import DiscordUserAuth

urlpatterns = [
    path('login/', DiscordUserAuth.as_view())
]
