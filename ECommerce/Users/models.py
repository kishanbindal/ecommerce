from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):

    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    phone_number = models.CharField(max_length=14, blank=False)

    # USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = [first_name, last_name, phone_number]
