from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_telegram_user = models.BooleanField(default=False, verbose_name='Is telegram user')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
