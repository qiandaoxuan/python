import urllib2
import urllib

url = 'http://www.baidu.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
values = {'name' : 'WHY',
          'location' : 'SDU',
          'language' : 'Python' }

data = urllib.urlencode(values)
print data
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page