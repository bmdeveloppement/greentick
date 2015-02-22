from django.contrib import admin
from request.models import Request, Answer, RequestValidator, File, Type

admin.site.register(Request)
admin.site.register(Answer)
admin.site.register(RequestValidator)
admin.site.register(File)
admin.site.register(Type)
