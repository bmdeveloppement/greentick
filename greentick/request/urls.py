from django.conf.urls import patterns, url

from request import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)