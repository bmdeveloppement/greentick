from django.db import models
from django.db.models import Q
from user.models import User, Company
from datetime import date
from request.extras import ContentTypeRestrictedFileField

ANSWER_CHOICES = (
    ('1', 'Yes'),
    ('2', 'Maybe'),
    ('3', 'No'),
)

TODAY = date.today()


class Type(models.Model):
    company = models.ForeignKey(Company, default=None, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    @staticmethod
    def get_for_user(user):
        return Type.objects.filter(Q(company=user.company) | Q(company=None)).all()


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
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    size = models.IntegerField()
    file = ContentTypeRestrictedFileField(upload_to='request_attachments/%s' % TODAY.strftime("%Y/%m/%d"))
