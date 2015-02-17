from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    subscription_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    company = models.ForeignKey(Company)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    subscription_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
