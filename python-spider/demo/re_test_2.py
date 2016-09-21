# -*- coding: utf-8 -*-


import re

pattern_a = re.compile(r'''\d + # 整数部分，匹配1到无限次
                           \.   # 小数点
                           \d + # 小数部分，匹配1到无限次
                        ''', re.X)
pattern_b = re.compile(r'\d+\.\d+')

match1_a = re.match(pattern_a, '3.04')
match2_a = re.match(pattern_a, '.3')
match3_a = re.match(pattern_a, '3.')

match1_b = re.match(pattern_b, '3.04')
match2_b = re.match(pattern_b, '.3')
match3_b = re.match(pattern_b, '3.')

if match1_a:
    print match1_a.group()
else:
    print 'match1_a匹配不成功'
if match2_a:
    print match2_a.group()
else:
    print 'match2_a匹配不成功'
if match3_a:
    print match3_a.group()
else:
    print 'match3_a匹配不成功'


if match1_b:
    print match1_b.group()
else:
    print 'match1_b匹配不成功'
if match2_b:
    print match2_b.group()
else:
    print 'match2_b匹配不成功'
if match3_b:
    print match3_b.group()
else:
    print 'match3_b匹配不成功'