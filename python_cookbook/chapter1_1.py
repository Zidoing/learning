#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime : 
# @Author   : Z LEI

# 字符串方法
import operator

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

"""
1.3 测试一个对象是否是类字符串
"""

print isinstance('string', basestring)
# TRUE

"""
1.4 字符串对齐
"""

print '|', 'hej'.ljust(20), '|', 'hej'.rjust(20), '|', 'hej'.center(20), '|'

# | hej                  |                  hej |         hej          |

"""
1.5 去除字符串两端的空格
"""

print "  fasfdasf  fasfas  ".strip()
# fasfdasf  fasfas

print "xyxxyy hejyx yyx".strip('xy')
#  hejyx

"""
1.6 字符串合并
"""

''.join(['a', 'b'])

print reduce(operator.add, ['a', 'b', 'c'])

"""
1.7 字符串逐字符或逐词翻转
"""

print 'abcdefghijklmnopqrstuvwxyz'[::-1]

a = list('abcdefghijklmnopqrstuvwxyz')
a.reverse()
print ''.join(a)

"""
1.8 检查字符串中是否包含某字符集合中的字符
"""

import itertools


def containAny(seq, aset):
    for item in itertools.ifilter(aset.__contains__, seq):
        return True
    return False


print
