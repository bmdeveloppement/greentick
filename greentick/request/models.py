from django.db import models
from user.models import User


class Request(models.Model):
    user = models.ForeignKey(User)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)  # @TODO : List : Holidays / Design / ...
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
    answer = models.CharField(max_length=5)  # @TODO : List : Yes / No / Maybe

    def __str__(self):
        return self.description


class RequestValidator(models.Model):
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)


class File(models.Model):
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    file = models.FileField(upload_to='downloads/',null=True)