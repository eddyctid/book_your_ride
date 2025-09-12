from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("mobile_num", "email", "is_staff", "is_active","is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser")

    #replace ordering to avoid username
    ordering = ("mobile_num",)

    # Fields shown when viewing/editing a user in admin
    fieldsets = (
        (None, {"fields": ("mobile_num", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields shown when creating a user in admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("mobile_num", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
