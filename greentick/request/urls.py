from django.conf.urls import patterns, url

from request import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.create, name='create'),
    url(r'^upload-file/(?P<request_id>\d+)/$', views.upload_file, name='upload-file'),
)