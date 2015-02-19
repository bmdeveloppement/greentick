from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    subscription_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class User(User):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company)
    job_title = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
