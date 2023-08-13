from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def _create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    USER_TYPE = (
        ('content_writer', 'BLoger'),
        ('student', 'Student'),
    )
    first_name = models.CharField(verbose_name="Name", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="Surname", max_length=255, blank=True)
    email = models.EmailField(verbose_name="Email", unique=False, blank=True)
    username = models.CharField(verbose_name="Username", max_length=255, unique=True)
    user_type = models.CharField(verbose_name="Type", max_length=255, choices=USER_TYPE, default="student")


    time_created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
