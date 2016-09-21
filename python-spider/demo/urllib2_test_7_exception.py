from urllib2 import Request, urlopen, URLError

req = Request('http://bbs.csdn.net/callmewhy')
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'code'):
        print 'the server couldn\'t fullfill the request'
        print e.code
    elif hasattr(e, 'reason'):
        print 'we failed reach the server'
        print 'reason is', e.reason
else:
    print 'everything is ok, no exception'