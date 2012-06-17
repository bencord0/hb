from django.http import HttpResponse
import datetime

def index (request):
    return HttpResponse("throb/index")

def ping(request):
    import socket
    now = datetime.datetime.now()
    me = "%s(%s)" % (
        request.META['SERVER_NAME'],
        "%s:%s"%(
            socket.gethostbyname(
                request.META['SERVER_NAME']),
                request.META['SERVER_PORT']))
    you = "%s(%s)" % (
        request.META['REMOTE_HOST'],
        request.META['REMOTE_ADDR'])
    html = "%s: %s %s" % (
        now,
        me,
        you)
    return HttpResponse(html)
