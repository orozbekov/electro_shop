from enum import unique
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from pyparsing import null_debug_action
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20, help_text="Пишите номер с кодом страны", unique=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    objects = CustomUserManager()