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
