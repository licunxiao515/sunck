from multiprocessing import Process,Pool # 进程池，进程池就是帮助管理的对象
import time

def foo(i):
    time.sleep(1)
    print(i)

if __name__ == '__main__':
    #实例化进程池
    pool = Pool(4)      #里边的值是多少代表能最大容量进程，异步4个4个输出。

    for i in range(10):
        pool.apply_async(foo,args=(i,))     #异步
        # pool.apply(foo,args=(i,))        #同步阻塞型，单进程模式
    pool.close() # 关闭以后就不能再创建新的进程了

    # 等待所有进程池的进程运行完毕
    pool.join()