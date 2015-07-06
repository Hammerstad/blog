from django.conf.urls import patterns, url

urlpatterns = patterns('app.blog.views',
    url(r'^$', 'home', name='home'),
    url(r'^post/(?P<id>\d+)$', 'view_post', name='view_post'),
    url(r'^post/new$', 'new_post', name='new_post'),
)