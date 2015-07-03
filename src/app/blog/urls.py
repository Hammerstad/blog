from django.conf.urls import patterns, url

urlpatterns = patterns('app.blog.views',
    url(r'^$', 'home', name='home'),
)