# This file is part of hb.
#
# hb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with hb.  If not, see <http://www.gnu.org/licenses/>.

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
