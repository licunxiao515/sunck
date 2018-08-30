import requests
from scrapy_test_0611.utils import mydb
from scrapy_test_0611 import settings
import threading        #多线程包
from queue import Queue

# 初始化数据库连接
mysql = settings.MYSQL_INFO
mysql = mydb.Mydb(mysql['MYSQL_HOST'], mysql['MYSQL_USER'], mysql['MYSQL_PASS'], mysql['MYSQL_DB'])

#获取所有数据库中所有代理ip,加入队列里
def get_proxy():
    proxy_q = Queue()       #代理队列
    sql = 'select * from xici'
    # query 方法 执行
    res = mysql.query(sql)
    #所有ip加入队列
    for proxy in res:
        proxy_q.put(proxy)
    #代理队列返回
    return proxy_q

#测试网站
class ProxyManager(threading.Thread):       #集成多线程
    base_url = 'http://www.baidu.com/s?wd=ip'

    def __init__(self,proxy_q,lock):
        super(ProxyManager,self).__init__() #继承父类
        self.proxy_q = proxy_q
        self.lock = lock        #初始化锁

    def run(self):      #run方法是在线程启动时调用
        while not self.proxy_q.empty():
            item = self.proxy_q.get()
            #开始创建一个代理
            proxy = {
                'http' : 'http://' + item['host'] + ':' +str(item['port']),
                'https' : 'https://' + item['host'] + ':' +str(item['port']),
            }

            #用代理发请求
            try :
                response = requests.get(self.base_url,proxies=proxy,timeout=3)#timeout=3，3秒超时就算异常
                print('可用%s %s' % (item['host'],item['port']))
            except Exception as e:
                with self.lock:     #with的作用是打开文件不用关闭
                    #如果请求异常，删除代理
                    self.drop_proxy(item)
                    print('链接超时')
            else:           #try完后，如果不走except走else,如果请求正常，再判断响应码
                if not (200 <= response.status_code <=300):#小于等于300，大于等于200
                    with self.lock:
                        self.drop_proxy(item)   # 删除代理
                        print(response.status_code)
    def drop_proxy(self,proxy):
        print('删除%s' % proxy['host'])
        sql = "delete from xici where host=%s"
        #执行
        mysql.execute(sql,(proxy['host']))

if __name__ == '__main__':
    proxy_q = get_proxy()  #实例化
    lock = threading.Lock() #mysql不能被多个线程同时访问，所以得加锁
    t_list = []
    for i in range(50):      #50个线程
        t = ProxyManager(proxy_q,lock)   #创建一个线程
        t.start()           #启动线程
        t_list.append(t)
    for t in t_list:
        t.join()        #阻塞

    #如果所有线程运行完毕，关闭数据库
    mysql.close()
