from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "mobile_num", "is_staff", "is_superuser", "is_active")
    list_filter = ("is_staff", "is_active", "is_superuser", "groups")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password", "mobile_num")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "mobile_num", "password1", "password2", "is_staff", "is_active")}
        ),
    )

    search_fields = ("email", "mobile_num")

admin.site.register(CustomUser, CustomUserAdmin)
