import urllib2

url = 'http://www.baidu.com'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
info = response.info()
print 'the info we get from server is:'
print info