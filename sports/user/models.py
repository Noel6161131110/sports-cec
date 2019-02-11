from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_enabled = models.BooleanField(default=True)
