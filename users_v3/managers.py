from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    
    def create_user(self, mobile_num, email, password, **extra_fields):
        if not mobile_num:
            raise ValueError("The mobile number must be set")
        if not email:
            raise ValueError("The email must be set")

        email = self.normalize_email(email)
        user = self.model(mobile_num=mobile_num, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, mobile_num, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(mobile_num, email, password, **extra_fields)