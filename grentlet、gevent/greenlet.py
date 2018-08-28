from greenlet import greenlet

def foo1():
    print(12)
    c2.switch()     #切换到协程2运行
    print(34)
    c2.switch()

def foo2():
    print(56)
    c1.switch()
    print(78)


c1 = greenlet(foo1)     #协程1
c2 = greenlet(foo2)     #协程2

c1.switch()     #switch() 启动协程