import urllib2

url = 'http://rrurl.cn/b1UZuP'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
real_url = response.geturl()
print 'the url we request is:' + url
print 'real url is:' + real_url