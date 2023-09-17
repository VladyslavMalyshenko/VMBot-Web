from typing import NamedTuple, Optional

from .models import User
from .discord import DiscordUserMixin


class UserData(NamedTuple):
    user: Optional[User] = None
    error: Optional[str] = None


class UserService:

    @classmethod
    def check_user_exists_by_fields(cls, fields: dict) -> bool:
        result = False
        for field, value in fields.items():
            try:
                result = User.objects.filter(**{field: value}).exists()
            except (Exception,):
                result = False
        return result

    def user_exists_by_discord_id(self, discord_id):
        return self.check_user_exists_by_fields({
            'discord_id': discord_id
        })

    @staticmethod
    def get_user_by_data(data: dict):
        try:
            return User.objects.get(**data)
        except User.DoesNotExist:
            return None


def get_user_by_discord_id(discord_id):
    try:
        return User.objects.get(discord_id=discord_id)
    except User.DoesNotExist:
        return None
