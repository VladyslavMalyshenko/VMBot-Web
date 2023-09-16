from rest_framework import serializers

from .models import User


class DiscordUserSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'username_with_tag',
                  'discord_id', 'avatar', 'email']
        read_only_fields = ['id']
