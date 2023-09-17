from rest_framework.response import Response

from .services import UserService
from rest_framework import status, generics

from django.shortcuts import redirect

from .serializers import UserSerializer, DiscordUserSerializer
from .services import (get_user_by_discord_id)
from .discord import PayloadAndHeadersMixin, DiscordUserMixin
from .jwt_auth import JwtAuthentication


class DiscordUserAuth(UserService,
                      DiscordUserMixin,
                      generics.GenericAPIView):
    serializer_class = DiscordUserSerializer

    def post(self, *args, **kwargs):
        discord_code = self.request.data.get('code')
        data = self.get_user(discord_code)

        if data is None:
            return Response({
                'Something went wrong... Please, try again.'
            }, status=status.HTTP_400_BAD_REQUEST)

        user_exists = self.user_exists_by_discord_id(data['discord_id'])
        login_data = {}

        if not user_exists:
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
        else:
            user = get_user_by_discord_id(data['discord_id'])
        login_data['discord_id'] = user.discord_id
        tokens = JwtAuthentication.get_jwt_auth(login_data)
        return Response(tokens, status=status.HTTP_200_OK)
