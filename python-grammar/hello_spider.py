# -*- coding: utf-8 -*-
#--------------------------------
#   程序：保存简单网页的小程序
#
#
#--------------------------------

import urllib2
import string

hds = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    'Referer': 'http://www.cnbeta.com/articles' #f反盗链
}

# 定义爬虫函数
def spider_url(url, file_name):
    print u'正在下载网页，并将其存储为' + file_name + '..........'
    f= open(file_name, 'w+')
    req = urllib2.Request(url, headers=hds)
    page = urllib2.urlopen(req).read()
    f.write(page)
    f.close()

url = raw_input(u'please input the page url：')
file_name = raw_input(u'please input file name：')
spider_url(url, file_name)
