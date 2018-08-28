from multiprocessing import Process,Manager
#Manager  数据共享,可以支持任意的对象类型

def foo(i,dic):
    dic[i] = i

if __name__ == '__main__':
    #初始化manager
    manager = Manager()
    # 专门给多进程共享的字典
    dic = manager.dict()
    
    pro_list = []
    for i in range(10):
        p = Process(target=foo,args=(i,dic))
        p.start()
        pro_list.append(p)

    for pro in pro_list:
        pro.join()

    print(dic)