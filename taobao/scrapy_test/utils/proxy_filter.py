import requests
from scrapy_test.utils import mydb
from scrapy_test import settings

#测试网站
class ProxyManager(object):
    base_url = 'http://www.baidu.com/s?wd=ip'

    def __init__(self):
        #初始化数据库连接
        mysql = settings.MYSQL_INFO
        self.mysql = mydb.Mydb(mysql['MYSQL_HOST'],mysql['MYSQL_USER'],mysql['MYSQL_PASS'],mysql['MYSQL_DB'])

    def proxy_filter(self):
        sql = 'select * from xici'
        #query 方法 执行
        res = self.mysql.query(sql)
        for item in res:
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
                #如果请求异常，删除代理
                self.drop_proxy(item)
                print('链接超时')
            else:           #try完后，如果不走except走else,如果请求正常，再判断响应码
                if not (200 <= response.status_code <=300):#小于等于300，大于等于200
                    self.drop_proxy(item)   # 删除代理
                    print(response.status_code)
    def drop_proxy(self,proxy):
        print('删除%s' % proxy['host'])
        sql = "delete from xici where host=%s"
        #执行
        self.mysql.execute(sql,(proxy['host']))

if __name__ == '__main__':
    pm =ProxyManager()  #实例化
    pm.proxy_filter()


