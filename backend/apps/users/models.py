from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150,
                                verbose_name='Username',
                                unique=True)
    username_with_tag = models.CharField(max_length=150,
                                         verbose_name='Username with tag',
                                         null=True,
                                         blank=True)
    discord_id = models.BigIntegerField(blank=True,
                                        null=True)
    avatar = models.URLField(blank=True,
                             null=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'User: {self.username}'

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.username_with_tag is not None:
                self.username = self.username_with_tag.strip('#')[0]
        super().save(*args, **kwargs)
