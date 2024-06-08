from django.contrib import admin

# Register your models here.
from .models import Contact, Subscription


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "email", "message", "created_at", "updated_at"]

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["email","is_subscribed", "created_at", "updated_at"]
    list_filter = ["is_subscribed", ]
    search_fields = ['email']

    