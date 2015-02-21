from django import forms
from django.core import validators
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=50)


class CreateUserForm(forms.Form):
    company = forms.CharField(label='Your company name', max_length=200)
    username = forms.CharField(label='Username', max_length=30)
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)
    job_title = forms.CharField(label='Job title', max_length=200)
    email = forms.EmailField(label='Email address', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=50)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username %(value)s is already in use',
                code='already_exists',
                params={'value': username},
            )

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < PASSWORD_MIN_LENGTH:
            raise forms.ValidationError(
                'Your password have to be %(value) characters or more',
                code='already_exists',
                params={'value': PASSWORD_MIN_LENGTH},
            )

        return password