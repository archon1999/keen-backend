from django.contrib.auth.models import AbstractUser
from django.db import models

from common.storages import UserAvatarStorage


class GenderChoice(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'


class User(AbstractUser):
    keencoin = models.IntegerField(default=0)
    avatar = models.ImageField(
        default='default_standart.webp',
        storage=UserAvatarStorage
    )
    gender = models.CharField(max_length=1, choices=GenderChoice.choices, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    students = models.ManyToManyField(to=Student)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
