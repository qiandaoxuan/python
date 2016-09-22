# -*- coding:utf-8 -*-

import urllib2
import re

def get_page(self, page_num):
    headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    qiubai_url = 'http://www.qiushibaike.com/hot/page/' + page_num
    req = urllib2.Request(qiubai_url, headers=headers)
    response = urllib2.urlopen(req)
    page = response.read().decode('utf-8')
    my_content = re.findall(r'<div class="content">.*?<span>(.*?)</span>', page, re.S)
    content = []
    for item in my_content:
        content.append(item.replace('<br/>', '\n'))
    return content
