from django.conf import settings
import requests

from .utils import get_encoded_url


class PayloadAndHeadersMixin:

    @staticmethod
    def get_payload(code):
        return {
            'client_id': settings.DISCORD_CLIENT_ID,
            'client_secret': settings.DISCORD_CLIENT_SECRET,
            'grant_type': settings.DISCORD_GRANT_TYPE,
            'code': code,
            'redirect_uri': settings.DISCORD_REDIRECT_URI,
            'scope': settings.DISCORD_SCOPE
        }

    @property
    def redirect_uri(self):
        return get_encoded_url(settings.DISCORD_REDIRECT_URI)

    @property
    def login_url(self):
        url = settings.DISCORD_LOGIN_URL.replace('{}', self.redirect_uri)
        return url

    @property
    def user_url(self):
        return f'{settings.DISCORD_API_URL}/users/@me'

    @property
    def _avatars_url(self):
        return 'https://cdn.discordapp.com/avatars/'

    @property
    def _avatars_url_embed(self):
        return 'https://cdn.discordapp.com/embed/avatars/'

    def get_user_avatar(
            self,
            user_id,
            avatar_code,
            discriminator=None
    ):
        if avatar_code is None:
            module = int(discriminator) % 5
            return f'{self._avatars_url_embed}{module}.png'
        return f'{self._avatars_url}{user_id}/{avatar_code}.png?size=2048'


class DiscordUserMixin(PayloadAndHeadersMixin):

    @staticmethod
    def _token_url_post(payload: dict):
        token = requests.post(
            url=settings.DISCORD_TOKEN_URL, data=payload).json()
        access_token = token.get('access_token')
        return access_token

    def get_access_token(self, code):
        payload = self.get_payload(code)
        return self._token_url_post(payload)

    def get_user_json(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(url=self.user_url, headers=headers)
        if response.status_code != 200:
            return None
        return response.json()

    def get_data_for_serializer(self, user_data: dict):
        return {
            'username': user_data['username'],
            'username_with_tag': user_data['discriminator'],
            'discord_id': user_data['id'],
            'avatar': self.get_user_avatar(
                user_data['id'],
                user_data['avatar'],
                user_data['discriminator']
            ),
            'email': user_data['email']
        }

    def get_user(self, code) -> dict | None:
        access_token = self.get_access_token(code)
        user = self.get_user_json(access_token)
        if user is not None:
            data = self.get_data_for_serializer(user)
            return data
        return None
