# -*- coding: utf-8 -*-
#--------------------------------
#   程序：百度贴吧爬虫，爬虫界的hello world
#
#
#--------------------------------

import urllib2
import string

# 定义爬虫函数
def spider_tieba(url, start_page, end_page):
    for i in range(start_page, end_page):
        file_name = string.zfill(i, 5) + '.html'
        print u'正在下载第' + str(i) + u'个网页，并将其存储为' + file_name + '..........'
        f= open(file_name, 'w+')
        page = urllib2.urlopen(url + str(i)).read()
        f.write(page)
        f.close()

#------------参数输入---------------

# python贴吧一个帖子地址
# spider_url = 'http://tieba.baidu.com/p/4606205714?pn='

#------------参数输入---------------

spider_url = raw_input(u'请输入要爬取的帖子地址（去掉pn=后面的内容）：')
begin_page = 1
end_page = 11
spider_tieba(spider_url, begin_page, end_page)
