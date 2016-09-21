import urllib2
import urllib

values = {'name' : 'WHY',
          'location' : 'SDU',
          'language' : 'Python' }
data = urllib.urlencode(values)
print data

url = 'http://www.baidu.com'
full_url = url + '?' + data
print full_url

req = urllib2.Request(full_url)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page