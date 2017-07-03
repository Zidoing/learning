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

"""
1.9  maketrans  对于字符串进行过滤，及讲某些字段转换成某个字段
"""

import string


def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('', '')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))

    def translate(s):
        return s.translate(trans, delete)

    return translate


digits_only = translator(delete=string.digits)
print digits_only('Chris Perkin : 224-7992')  # Chris Perkin : -
digits_only = translator(keep=string.digits)
print digits_only('Chris Perkin : 224-7992')  # 2247992

"""
1.10 过滤字符串中不属于指定集合的字符
"""

import string

allchars = string.maketrans('', '')


def makefilter(keep):
    delchars = allchars.translate(allchars, keep)

    def thefilter(s):
        return s.translate(allchars, delchars)

    return thefilter


"""
1.11 检查一个字符串是文本还是二进制
"""
import string

text_characters = "".join(map(chr, range(32, 127))) + '\n\r\t\b'
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
print text_characters
_null_trans = string.maketrans("", "")


def istext(s, text_characters=text_characters, threshold=0.30):
    if "\0" in s:
        return False
    if not s:
        return True
    t = s.translate(_null_trans, text_characters)
    return len(t) / len(s) <= threshold


"""
1.12 控制大小写AAA
"""

print 'one tWo thrEe'.capitalize()
print 'one tWo thrEE'.title()
print '>>>>>>>>>>>>'
"""
1.13 访问子字符串
"""

"""
1.14 改变多行文本字符串的缩进
"""


def reindent(s, numSpaces):
    leading_space = numSpaces * ' '
    lines = [leading_space + line.strip() for line in s.splitlines()]
    return '\n'.join(lines)


x = """ line one
    line two   
and line three
"""
print x
#  line one
#     line two
# and line three
print reindent(x, 4)


# line one
# line two
# and line three


def addSpaces(s, numAdd):
    white = " " * numAdd
    return white + white.join(s.splitlines(True))


def numSpaces(s):
    return [len(line) - len(line.lstrip()) for line in s.splitlines()]


def delSpaces(s, numDel):
    if numDel > min(numSpaces(s)):
        raise ValueError, "removing more spaces than there are!"
    return '\n'.join([line[numDel:] for line in s.splitlines()])


def unIndentBlock(s):
    return delSpaces(s, min(numSpaces(s)))


print addSpaces(x, 4)
print numSpaces(x)
print unIndentBlock(x)

"""
1.15 扩展和压缩制表符
"""

x = '''\tdafas\tfasdf\tdsafsad\tadfsafsa
fda\tfdasf\tfdsa
'''
mystring = x.expandtabs()
print mystring
mystring = x.expandtabs(2)
print mystring


def unexpand(astring, tablen=8):
    import re
    pieces = re.split(r'( +)', astring.expandtabs(tablen))
    lensofar = 0
    for i, piece in enumerate(pieces):
        thislen = len(piece)
        lensofar += thislen
        if piece.isspace():
            numblanks = lensofar % tablen
            numtabs = (thislen - numblanks + tablen - 1) / tablen
            pieces[i] = '\t' * numtabs + ' ' * numblanks
    return ''.join(pieces)


"""
1.16 替换字符串中的子串
"""


def expand(format, d, marker='"', safe=False):
    if safe:
        def lookup(w):
            return d.get(w, w.join(marker * 2))
    else:
        def lookup(w):
            return d[w]
    parts = format.split(marker)
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)


"""
1.17 替换字符串中的子串 python2.4
"""

import string

new_style = string.Template('this is $thing')
print new_style.substitute({'thing': 5})
print new_style.substitute({'thing': 'test'})
print new_style.substitute(thing=5)
print new_style.substitute(thing='test')

"""
1.18 一次完成多个替换
"""
import re


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    return rx.sub(one_xlat, text)


"""
1.19 检查字符串中的结束标记

English is not my native language ,please excuse  typing error
"""
import itertools


def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)


def endWith(s, *endings):
    return anyTrue(s.endswith, endings)


'''
打印出当前目录下所有的图片文件
'''
import os

for filename in os.listdir('.'):
    if not endWith(filename, '.jpg', '.jepg', '.gif'):
        print filename

german_ae = unicode('\xc3\xa4', 'utf-8')
print german_ae

"""
1.21 在 unicode和普通字符串之间转换
"""
uncodestring = u'hello workld'
utf8string = uncodestring.encode('utf-8')
print utf8string
asciistring = uncodestring.encode('ascii')
print asciistring
isostring = uncodestring.encode('ISO-8859-1')
print isostring
utf16string = uncodestring.encode('utf-16')
print utf16string

plainstring1 = unicode(utf8string, 'utf-8')
plainstring2 = unicode(asciistring, 'ascii')
plainstring3 = unicode(isostring, 'ISO-8859-1')
plainstring4 = unicode(utf16string, 'utf-16')
print plainstring1, plainstring2, plainstring3, plainstring4

"""
1.22 在标准输出中打印Unicode字符
"""
import codecs, sys

sys.stdout = codecs.lookup('iso8859-1')[-1](sys.stdout)

if __name__ == '__main__':
    # print expand('just "a" test', {"x": "one"}, safe=True)
    pass
