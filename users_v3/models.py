from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"),unique=True)
    mobile_num = models.CharField(_("mobile number"),max_length=15, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "mobile_num"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.mobile_num
    
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"