from django.db import models

from users.models import User


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_contacts",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    is_subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email
    
    