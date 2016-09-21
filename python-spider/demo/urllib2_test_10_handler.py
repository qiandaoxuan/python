#! -*- encoding:utf-8 -*-
import urllib2

url = 'http://www.baidu.com'

#HTTPHandler方式
opener1 = urllib2.OpenerDirector()
handler1 = urllib2.HTTPHandler()
opener1.add_handler(handler1)
response1 = opener1.open(url,timeout=10)
print response1.read()

#FileHandler方式
opener3 = urllib2.FileHandler()
handler3 = urllib2.build_opener(opener3)
req = urllib2.Request(url=r'file:/F:\workdir\test.txt')
response3 = opener3.open_local_file(req)
print response3.read()

#ProxyHandler方式
handler2 = urllib2.ProxyHandler(proxies = {'http' : 'http://217.66.205.76:8080/'})
opener2 = urllib2.build_opener(handler2)
response2 = opener2.open(url,timeout=5)
#urllib2.install_opener(opener2) install_opener会设置全局opener,如不希望,用opener2.open()
print response2.read()

#FtpHandler方式类似，不再举例




