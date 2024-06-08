from django import forms
from .models import Contact, Subscription
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput())
    email = forms.EmailField(max_length=100, widget=forms.EmailInput())
    message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ("name", "email", "message")

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Subscription.objects.filter(email=email).exists():
            raise ValidationError("Email already subscribed", code="email_exists")
        return email

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
    


    