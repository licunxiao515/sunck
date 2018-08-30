from fake_useragent import UserAgent
import random
import base64
from scrapy.conf import settings
class RandomUserAgent(object):      #继承object
    def __init__(self,cralwer):     ##初始化useragent,接收cralwer
        self.ua = UserAgent()
        #全局爬虫对象
        self.crawler = cralwer

    @classmethod        #变成类方法
    def from_crawler(cls,cralwer): #定义一个方法
        return cls(cralwer)                   #实例化一个对象,返回


    def process_request(self,request,spider):
        # ua_type = settings['UA_TYPE']         #获取值
        #getattr 获取ua对象下的某一个属性
        # print(self.crawler.settings['UA_TYPE'])     #输出结果是random,说明是自己配置的
        ua= getattr(self.ua,self.crawler.settings['UA_TYPE'])
        # ua = getattr(self.ua,ua_type)             #获取属性，生成浏览器标识
        # request.headers.setdefault('User-Agent',ua)     #指定哪个请求头，什么值
        request.headers['User-Agent'] = ua              #和上边方法一样

#代理
class RandomProxy(object):
    def __init__(self, cralwer):  ##初始化useragent,接收cralwer
        # 全局爬虫对象
        self.crawler = cralwer

    @classmethod  # 变成类方法
    def from_crawler(cls, cralwer):  # 定义一个方法
        return cls(cralwer)  # 实例化一个对象,返回

    def process_request(self,request,spider):
        proxies = self.crawler.settings['PROXIES']  #拿到一个代理
        proxy = random.choice(proxies)  #随机拿到一个代理

        request.meta['proxy'] = proxy['host']   ###设置代理

# #认证代理
# class AuthRandomProxy(object):
#     def __init__(self, cralwer):  ##初始化useragent,接收cralwer
#         # 全局爬虫对象
#         self.crawler = cralwer
#
#     @classmethod  # 变成类方法
#     def from_crawler(cls, cralwer):  # 定义一个方法
#         return cls(cralwer)  # 实例化一个对象,返回
#
#     def process_request(self,request,spider):
#         proxies = self.crawler.settings['AUTH_PROXIES']  # 获取代理
#         proxy = random.choice(proxies)              #随机获取一个代理
#
#         #设置认证信息（用户名和密码）
#         auth = proxy['auth']
#         auth = base64.b64encode(bytes(auth,'utf-8'))    #转换成base64类型
#         request.headers['Proxt-Authorezation'] = b'Basic ' + auth     #设置请求头部,认证信息
#
#
#         #设置代理ip和端口号
#         request.meta['proxy'] = proxy['host']