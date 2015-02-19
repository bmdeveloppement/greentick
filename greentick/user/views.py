from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the HomePage.")

def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)
