import multiprocessing
from multiprocessing import Process
import time

# 进程函数
def foo(i):
    time.sleep(1)       #一秒执行一次
    print(i)

# 创建进程一定要在 __name__ == __main__ 条件成立下
if __name__ == '__main__':
    # 默认形况下，主进程等待所有子进程城运行完毕
    print(time.ctime())         #获取时间

    pro_list = []
    for i in range(100):
        #创建一个子进程
        p = Process(target=foo,args=(i,))   #Process函数,target进程函数对象，args传入的是元祖
        pro_list.append(p)      #把子进程收集起来
        p.daemon = False  # 默认daemon 是False，等待子进程   如果设置为True,主进程不等子进程执行完毕就结束
        p.start()       #运行进程

    # # 等待所有子进程运行完毕才继续执行
    for pro in pro_list:
        pro.join()          #阻塞主进程

    print(time.ctime())
