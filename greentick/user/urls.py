from django.conf.urls import patterns, url

from user import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    # ex: /user/5/
    url(r'^edit/(?P<user_id>\d+)/$', views.edit, name='edit'),
)