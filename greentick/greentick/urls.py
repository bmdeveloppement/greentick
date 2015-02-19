from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'greentick.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('user.urls', namespace='user')),
    url(r'^user/', include('user.urls', namespace='request')),
    url(r'^request/', include('request.urls', namespace='user')),
)
