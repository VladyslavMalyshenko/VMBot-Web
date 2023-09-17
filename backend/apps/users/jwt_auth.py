import jwt

from enum import Enum

from datetime import datetime

from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class TokenTypes(str, Enum):
    access_token = 'access_token'
    refresh_token = 'refresh_token'


class JwtAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return None

        jwt_token = JwtAuthentication.get_token_from_header(jwt_token)

        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')

        identification_data = payload.get('identification')
        user = User.objects.filter(**identification_data).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        return user, payload

    def authenticate_header(self, request):
        return settings.AUTH_HEADER

    @staticmethod
    def _get_token_payload(
            identification_data: dict,
            token_type: TokenTypes = TokenTypes.access_token,
    ):
        lifetime = settings.ACCESS_TOKEN_LIFETIME
        if token_type == TokenTypes.refresh_token:
            lifetime = settings.REFRESH_TOKEN_LIFETIME
        return {
            'exp': int((datetime.now() + lifetime).timestamp()),
            'iat': datetime.now().timestamp(),
            'identification': identification_data
        }

    @staticmethod
    def get_encoded_token(payload):
        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        return token

    @classmethod
    def create_access_token(cls, data: dict):
        payload = cls._get_token_payload(data, TokenTypes.refresh_token)
        return cls.get_encoded_token(payload)

    @classmethod
    def create_refresh_token(cls, data: dict):
        payload = cls._get_token_payload(data, TokenTypes.refresh_token)
        return cls.get_encoded_token(payload)

    @classmethod
    def get_jwt_auth(cls, identification_data):
        return {
            'access_token': cls.create_access_token(identification_data),
            'refresh_token': cls.create_refresh_token(identification_data)
        }

    @classmethod
    def get_token_from_header(cls, token):
        token = token.replace(settings.AUTH_HEADER, '').replace(' ', '')  # clean the token
        return token
