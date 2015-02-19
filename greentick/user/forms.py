from django import forms


class LoginUserForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=50)


class CreateUserForm(forms.Form):
    company = forms.CharField(label='Your company name', max_length=200)
    first_name = forms.CharField(label='First name', max_length=200)
    last_name = forms.CharField(label='Last name', max_length=200)
    job = forms.CharField(label='Job title', max_length=200)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=50)
