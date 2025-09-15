from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


def modified_normalize_email(email):
        """
        Normalize the email address by lowercasing it.
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name.lower() + "@" + domain_part.lower()
        return email
    
class CustomUserManager(BaseUserManager):
    """
        Defines how the User(or the model to which attached) will create users and superusers.
    """
    def create_user(self, mobile_num, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        
        if not mobile_num:
            raise ValueError(_("Mobile number must be set"))
        
        print(email)
        email = modified_normalize_email(email) # lowercase the domain
        print(email)

        if self.model.objects.filter(email=email).exists():
            raise ValueError(_("This email is already registered"))

        user = self.model(
            mobile_num=mobile_num,
            email=email,
            **extra_fields
        )

        user.set_password(password) # hash raw password and set

        user.save()

        return user
    
    def create_superuser(self, mobile_num, email, password, **extra_fields):
        """
        Create and save a superuser with the given email, 
        password, and date_of_birth. Extra fields are added
        to indicate that the user is staff, active, and indeed
        a superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(mobile_num, email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    mobile_num = models.CharField(max_length=15, unique=True)
    
    USERNAME_FIELD = "mobile_num"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower().strip()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.email