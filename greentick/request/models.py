from django.db import models
from user.models import User, Company

ANSWER_CHOICES = (
    ('1', 'Yes'),
    ('2', 'Maybe'),
    ('3', 'No'),
)


class Type(models.Model):
    company = models.ForeignKey(Company, default=None, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Request(models.Model):
    user = models.ForeignKey(User)
    type = models.ForeignKey(Type)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    tracking_reference = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    answer = models.PositiveSmallIntegerField(choices=ANSWER_CHOICES)

    def __str__(self):
        return self.description


class RequestValidator(models.Model):
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)


class File(models.Model):
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    file = models.FileField(upload_to='')
