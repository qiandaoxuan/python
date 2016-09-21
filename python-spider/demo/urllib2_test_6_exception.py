from urllib2 import Request, urlopen, HTTPError, URLError

req = Request('http://www.baibai.com')
try:
    response = urlopen(req)
except HTTPError as e:
    print 'the server couldn\'t fullfill the request'
    print 'error code', e.code
except URLError as e:
    print 'we failed reach the server'
    print 'reason is', e.reason
else:
    print 'everything is ok, no exception'

