# -*- coding: utf-8 -*-

import urllib2
from urllib2 import URLError
import re
import time
import thread

class Spider_Model:
    def __init__(self):
        self.flag = True
        self.pages = []
        self.page_num = 1
    def get_content(self, page_num):
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        qiubai_url = 'http://www.qiushibaike.com/hot/page/' + str(page_num)
        req = urllib2.Request(qiubai_url, headers=headers)
        response = urllib2.urlopen(req)
        page = response.read()
        my_content = re.findall(r'<a href="/users/.*?title="(.*?)">.*?<div class="content">.*?<span>(.*?)</span>', page,
                                re.S)
        content = []
        for item in my_content:
            content.append([item[0], item[1].replace('<br/>', '\n')])
        return content
    def load_page(self):
        while self.flag:
            if len(self.pages) < 2:
                try:
                    self.page_num += 1
                    self.pages.append(self.get_content(self.page_num))
                except URLError as e:
                    print '无法连接糗百！！！'
                    print e.code
                    print e.reason
            else:
                 time.sleep(1)

    def show_page(self, current_page, page_num):
        for item in current_page:
            print '<第%d页 id:%s>' %(page_num, item[0])
            print item[1] + '\n'
    def start(self):
        show_num = self.page_num
        thread.start_new_thread(self.load_page,())
        print u'正在加载中，请稍后......\n'
        while self.flag:
            if self.pages:
                self.show_page(self.pages[0], show_num)
                del self.pages[0]
                show_num += 1
                user_input = raw_input()
                if user_input == '\n':
                    self.flag = True
                elif user_input == 'quit':
                    self.flag = False
                    break

#--------------程序入口-----------------------
print u'''
---------------------------------------------
    程序：糗事百科爬虫
    版本：0.2
    作者：jijfe01
    功能：浏览近日热门糗事
    操作：回车继续浏览，输入quit退出浏览程序
    思路：在0.1的基础上改进，单启一个线程抓取网页，显示时从库里读取，提高速度
---------------------------------------------
'''
#--------------------------------------------
spider = Spider_Model()
spider.start()






