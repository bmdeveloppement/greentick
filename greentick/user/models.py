from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    subscription_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    company = models.ForeignKey(Company)
    job_title = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    @staticmethod
    def get_by_company(company):
        return User.objects.filter(company=company).all()