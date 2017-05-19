#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime : 
# @Author   : Z LEI

# 字符串方法
print '13213'.isdigit()  # 纯数字
print '1323fdasf13'.isalnum()  # 字符数字
print 'sssss'.isalpha()  # 纯字符
print 'sssx'.islower()  # 小写
print ' '.isspace()  # 是否是空
print 'AAAA'.isupper()  # 是否大写
print 'Title'.istitle()  # 是否开头为大写

"""
 1.1 每次处理一个字符
"""
str = 'a am a good boy'
print list(str)
for i in str:
    print i
print [i for i in str]
a = set('aaaffff')
b = set('fasdfasxxxxdfasf')
print a, b
print a & b  # 2个交集
# set(['a', 'f']) set(['a', 'x', 's', 'd', 'f'])
# set(['a', 'f'])


"""
1.2 字符和字符值之间的转换
"""
print ord('a')
# >> 97
print chr(97)
# >> a

# unicode 码值最大 65535
print ord(u'\u2020')
# 8224
print unichr(8224)
print repr(unichr(8224))
# †
# u'\u2020'

print ''.join(map(chr, range(1, 128)))
#
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
