from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "your username",
                "class": "px-6 py-3 w-full rounded-xl",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "your password",
                "class": "px-6 py-3 w-full rounded-xl",
            }
        )
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "your username",
                "class": "px-6 py-3 w-full rounded-xl",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": " your email address",
                "class": "px-6 py-3 w-full rounded-xl",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "your password",
                "class": "px-6 py-3 w-full rounded-xl",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "confirm your password",
                "class": "px-6 py-3 w-full rounded-xl",
            }
        )
    )
