# -*- coding:utf-8 -*-

import urllib2
import re

def get_page(page_num):
    headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    qiubai_url = 'http://www.qiushibaike.com/hot/page/' + str(page_num)
    req = urllib2.Request(qiubai_url, headers=headers)
    response = urllib2.urlopen(req)
    page = response.read()
    my_content = re.findall(r'<a href="/users/.*?title="(.*?)">.*?<div class="content">.*?<span>(.*?)</span>', page, re.S)
    content = []
    for item in my_content:
        content.append([item[0], item[1].replace('<br/>', '\n')])
    return content
def show_page():
    page_num = 1
    flag = True
    while flag:
        page_content = get_page(page_num)
        for item in page_content:
            print '<第' + str(page_num) + '页 ' + 'id:' + item[0] + '>'
            print item[1] + '\n'
        page_num += 1
        user_input = raw_input()
        if user_input == '\n':
            flag = True
        elif user_input == 'quit':
            flag =False

#--------------程序入口-----------------------
print u'''
---------------------------------------------
    程序：糗事百科爬虫
    版本：0.1
    作者：jijfe01
    功能：浏览近日热门糗事
    操作：回车继续浏览，输入quit退出浏览程序
    思路：需要展示下一页时去网站爬取下一页再展示出来，上网获取，所以浏览速度不佳
---------------------------------------------
'''
#--------------------------------------------
show_page()




