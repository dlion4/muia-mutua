from django.contrib import admin

# Register your models here.
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "email", "message", "created_at", "updated_at"]
