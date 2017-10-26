
import threading
import time


begin = time.time()


def foo(n):
    time.sleep(1)
    print "foo%s" % n


def bar(n):
    time.sleep(2)
    print "bar%s" % n


t1 = threading.Thread(target=foo, args=(1,))

t2 = threading.Thread(target=bar, args=(2,))


t1.start()

t2.start()



for i in range(10):
	print i



print i
print i