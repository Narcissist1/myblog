from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blogengine.views.getRecentPosts'),
    url(r'^(?P<selected_page>\d+)/?$','blogengine.views.getPosts'),
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),
    url(r'', include('django.contrib.flatpages.urls')),
)
