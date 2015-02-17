from django.contrib import admin
from request.models import Request, Answer, RequestValidator

admin.site.register(Request)
admin.site.register(Answer)
admin.site.register(RequestValidator)
