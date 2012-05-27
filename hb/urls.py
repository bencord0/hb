from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^hb/', include('hb.foo.urls')),
    url(r'^ping/', 'hb.views.ping'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
