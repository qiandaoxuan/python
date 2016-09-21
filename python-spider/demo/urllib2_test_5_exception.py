import urllib2

req1 = urllib2.Request('http://www.baibai.com')
req2 = urllib2.Request('http://bbs.csdn.net/callmewhy')
try:
    request = urllib2.urlopen(req1)
except urllib2.URLError as e:
    print e.reason

try:
    request = urllib2.urlopen(req2)
except urllib2.HTTPError as e:
    print e.code