from django.contrib.auth.models import AbstractUser
from django.db import models

from common.storages import UserAvatarStorage


class User(AbstractUser):
    keencoin = models.IntegerField(default=0)
    avatar = models.ImageField(
        default='default_standart.webp',
        storage=UserAvatarStorage
    )
