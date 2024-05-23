from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput())
    email = forms.EmailField(max_length=100, widget=forms.EmailInput())
    message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ("name", "email", "message")
