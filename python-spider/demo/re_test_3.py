# -*- coding: utf-8 -*-

import re

m = re.match(r'(\w+) (\w+)(?P<sign>.?)', 'hello world! hello you!')

print 'm.string:', m.string                                     #匹配时使用的文本
print 'm.re:', m.re                                             #匹配时使用的pattern对象
print 'm.pos:', m.pos                                           #文本中正则表达式开始搜索的索引
print 'm.endpos:', m.endpos                                     #文本中正则表达式结束搜索的索引
print 'm.lastindex:', m.lastindex                               #最后一个被捕获的分组在文本中的索引
print 'm.lastgroup:', m.lastgroup                               #最后一个被捕获的分组的别名

print 'm.group:', m.group()                                     #返回一个或多个分组捕获的字符串，可指定参数指定哪个分组捕获的字符串，如下
print 'm.group(1,2)', m.group(1,2)
print 'm.groups():', m.groups()                                 #以元组形式返回全部分组捕获的字符串，相当于group(1,2...,last)
print 'm.groupdict():', m.groupdict()                           #返回以有别名的组的别名为键、以该组截获的子串为值的字典
print 'm.start():', m.start(2)                                  #返回指定的组截获的子串在string中的起始索引
print 'm.end():', m.end(2)                                      #返回指定的组截获的子串在string中的结束索引
print 'm.span():', m.span(2)                                    #返回(start(group), end(group))
print "m.expand('\g<2> \g<1>\g<3>'):", m.expand(r'\2 \1\3')     #将匹配到的分组代入template中然后返回





