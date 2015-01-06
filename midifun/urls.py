from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'midifun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$', views.list_songs),
    url(r'^play/(.*)', views.play),
    url(r'^event/(.*)/(.*)/(.*)', views.event2),
    url(r'^event/(.*)/(.*)', views.event1),
    url(r'^event/(.*)', views.event0),
    url(r'^tone/(.*)/(.*)', views.tone),
    url(r'^stop', views.stop),
    url(r'^admin/', include(admin.site.urls)),
)
