from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    subscription_date = models.DateTimeField(auto_now=False, auto_now_add=True)


class User(models.Model):
    company = models.ForeignKey(Company)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subscription_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True, auto_now_add=False)
