from django.views.generic import RedirectView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='/throb/')),
    url(r'^index$', 'hb.views.index'),
    (r'^throb/', include('throb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
