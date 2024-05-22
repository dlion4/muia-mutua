from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from django import forms


class UserAdminCreationForm(UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)
        error_messages = {
            "email": {"unique": "This email has already been taken."},
        }


class UserAdminChangeForm(UserChangeForm):
    """
    Form for User Change in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta:
        model = User
        fields = ("email",)
        error_messages = {
            "email": {"unique": "This email has already been taken."},
        }


class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
