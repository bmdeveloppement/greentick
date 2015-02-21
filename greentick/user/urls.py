from django.conf.urls import patterns, url

from user import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.create, name='create'),
    # ex: /user/5/
    url(r'^edit/(?P<user_id>\d+)/$', views.edit, name='edit'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
)