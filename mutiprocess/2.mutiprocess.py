from multiprocessing import Process,Manager,Queue
# from queue import Queue
import time

def foo(i,q):
    q.put(i)        #往队列里添加值
    #print()
if __name__ == '__main__':
    print(time.ctime())
    q = Queue() # 初始化一个队列

    pro_list = []
    for i in range(10):
        #创建一个子进程
        p = Process(target=foo,args=(i,q))
        p.start()
        pro_list.append(p)

    for pro in pro_list:
        pro.join()

    # print(q.qsize()) #输出Queue()里有多少元素

    #Queue队列的作用是确保子进程都完成后再输出主进程,数据共享
    # 最后获取q的结果
    while not q.empty():    #非空，q.empty()判断队列里是否为空
        print(q.get())      #Queue.get()函数是个默认阻塞的函数，如果队列为空，会一直等待

    print(time.ctime())