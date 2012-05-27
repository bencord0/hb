from django.http import HttpResponse
import datetime

def ping(request):
    import socket
    now = datetime.datetime.now()
    me = socket.gethostbyname(socket.gethostname())
    you = request.get_host()
    html = "%s: %s %s" % (now, me, you)
    return HttpResponse(html)
