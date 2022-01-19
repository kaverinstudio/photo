from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    city = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        full_name = self.get_full_name()

        if full_name:
            return f'{full_name} ({self.email})'

        return f'{self.username} ({self.email})'

    def get_pretty_name(self):
        full_name = self.get_full_name()
        if full_name:
            return full_name

        return self.username
