from django.conf.urls import patterns, include, url

urlpatterns = patterns('throb.views',
    url(r'^$', 'ping'),
    url(r'^index/$', 'index'),
)
