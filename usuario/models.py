from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import logging


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("usuario:profile", kwargs={"pk": self.pk})
