from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("mobile_num", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("mobile_num", "email")