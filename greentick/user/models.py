from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    subscription_date = models.DateTimeField(auto_now=False, auto_now_add=True)


class User(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    company = models.ForeignKey(Company)
    job_title = models.CharField(max_length=200)
