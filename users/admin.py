from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User


@admin.register(User)
class useradminReq(UserAdmin):
    # list_display = ["email", "is_active", "is_staff", "is_superuser", "date_joined"]
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User
    list_display = ["email", "is_active", "is_staff", "is_superuser", "date_joined"]
    list_filter = ["email", "is_active", "is_staff", "is_superuser", "date_joined"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("date_joined",)
