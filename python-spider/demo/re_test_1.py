# -*- coding: utf-8 -*-
import re

pattern = re.compile(r'hello')

match1 = pattern.match('hello world')
match2 = pattern.match('helloo world')
match3 = pattern.match('heloo world')

match4 = re.match('hello', 'helloworld')

if match1:
    print match1.group()
else:
    print 'match1匹配失败'
if match2:
    print match2.group()
else:
    print 'match2匹配失败'
if match3:
    print match3.group()
else:
    print 'match3匹配失败'

if match4:
    print match4.group()
else:
    print 'match4匹配失败'