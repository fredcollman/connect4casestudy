from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):
    username = forms.CharField(
        label='User name',
        widget=forms.TextInput,
    )

    password2 = forms.CharField(
        label=("Confirm password"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
