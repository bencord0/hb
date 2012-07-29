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

from django.http import HttpResponse
import datetime

def index (request):
    return HttpResponse("throb/index")

def ping(request):
    import socket
    now = datetime.datetime.now()
    me = "%s(%s)" % (
        request.META.get('SERVER_NAME', ''),
        "%s:%s"%(
            socket.gethostbyname(request.META.get('SERVER_ADDR', '')),
            request.META.get('SERVER_PORT', '')
        )
    )
    you = "%s(%s)" % (
        request.META.get('REMOTE_HOST', ''),
        "%s:%s"%(
            request.META.get('REMOTE_ADDR',''),
            request.META.get('REMOTE_PORT', '')
        )
    )
    html = "%s: %s %s" % (
        now, me, you)
    return HttpResponse(html)
