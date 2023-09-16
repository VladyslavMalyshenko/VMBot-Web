import os

import requests

from django.conf import settings
from dotenv import load_dotenv

from .utils import get_encoded_url

load_dotenv()


class PayloadHeadersMixin:

    @staticmethod
    def get_payload(code):
        return {
            'client_id': os.getenv('DISCORD_CLIENT_ID'),
            'client_secret': os.getenv('DISCORD_CLIENT_SECRET'),
            'grant_type': os.getenv('DISCORD_GRANT_TYPE'),
            'code': code,
            'redirect_uri': os.getenv('DISCORD_REDIRECT_URI'),
            'scope': os.getenv('DISCORD_SCOPE')
        }

    @property
    def redirect_uri(self):
        return get_encoded_url(os.getenv('DISCORD_REDIRECT_URI'))

    @property
    def login_url(self):
        url = os.getenv('DISCORD_LOGIN_URL').replace('{}', self.redirect_uri)
        return url

    @property
    def user_url(self):
        return f'{os.getenv("DISCORD_API_URL")}/users/@me'

    @staticmethod
    def get_user_avatar(user_id, avatar_code):
        return f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_code}.png?size=2048'


class DiscordUserMixin(PayloadHeadersMixin):

    @staticmethod
    def _token_url_post(payload: dict):
        token = requests.post(url=os.getenv('DISCORD_TOKEN_URL'), data=payload).json()
        access_token = token.get('access_token')
        return access_token

    def get_access_token(self, code):
        payload = self.get_payload(code)
        return self._token_url_post(payload)

    def get_user_json(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        user_data = requests.get(url=self.user_url, headers=headers).json()
        return user_data

    def get_data_for_serializer(self, user_data: dict):
        return {
            'username': user_data['username'],
            'username_with_tag': user_data['discriminator'],
            'discord_id': user_data['id'],
            'avatar': self.get_user_avatar(user_data['id'], user_data['avatar']),
            'email': user_data['email']
        }

    def get_user(self, code):
        access_token = self.get_access_token(code)
        user = self.get_user_json(access_token)
        data = self.get_data_for_serializer(user)
        print(data)
        return data
