import re

print re.findall('w\w{2}l', 'hello world')

print re.findall('[a-z]', 'adfdasf')

print re.findall('[^com]', 'com')
print re.findall('\w', 'com')
print re.search('\w', 'com').group()

print re.search('f(as)|ff', 'sdjkfasasff').group()

ret = re.search('(?P<id>\d{3})(?P<name>\w{3})', 'dsafsf33343fda')
print ret.group()
print ret.group('id')
print ret.group('name')

print re.split('1', '1sdjksal')


print {i for i in range(10)}


class A(object):

    @property
    def per(self):
        return 1

    @per.setter
    def per(self, val):
        print val


a = A()
print a.per
a.per = 2


### python 单例模式
