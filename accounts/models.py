from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    wallet_addr = models.CharField(max_length=42)