from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogengine.views import PostsFeed

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #admin page
    url(r'^admin/',include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #Home page
    url(r'^$','blogengine.views.getPosts'),
    url(r'^(?P<selected_page>\d+)/?$','blogengine.views.getPosts'),
    #Blog posts
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),
    #Categories
    url(r'^categories/(?P<categorySlug>\w+)/?$','blogengine.views.getCategory'),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$','blogengine.views.getCategory'),
    # Comments
    url(r'^comments/', include('django.contrib.comments.urls')),
    # RSS feeds
    url(r'^feeds/posts/$', PostsFeed()),
    #Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
)
