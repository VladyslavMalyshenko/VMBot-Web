import random

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150,
                                verbose_name='Username',
                                unique=True)
    username_with_tag = models.CharField(max_length=150,
                                         verbose_name='Username with tag')
    discord_id = models.BigIntegerField(unique=True)
    avatar = models.URLField(blank=True,
                             null=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'User: {self.username}'

    def save(self, *args, **kwargs):
        if self._state.adding and self.is_staff:
            random_id = str(random.randint(1000000, 101000000000))
            self.discord_id = int(random_id)
        super().save(*args, **kwargs)
