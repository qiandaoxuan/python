import urllib2
import cookielib

cookie = cookielib.CookieJar()
print cookie
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
print 'return code is:' + str(response.code)
print cookie
for item in cookie:
    print 'name:' + item.name
    print 'value:' + item.value