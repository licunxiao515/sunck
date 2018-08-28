import gevent
from gevent import monkey
# 打补丁，替换python标准库中的模块（如果不打补丁，可能实现不了协程间的切换）
monkey.patch_all()      #有IO操作时需要这一句
import time

# 协程函数
def foo1(i):
    time.sleep(1)
    print(i)

g_list = []
for i in range(10):
    g = gevent.spawn(foo1,i)        #创建协程
    g_list.append(g)                #协程加入列表里

print(time.ctime())
gevent.joinall(g_list)      #运行协程，并等待协程运行完毕
print(time.ctime())
