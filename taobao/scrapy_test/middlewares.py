# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from scrapy_test.utils import mydb
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time

class RandomProxy(object):
    def __init__(self, cralwer):  ##初始化useragent,接收cralwer
        # 全局爬虫对象
        self.crawler = cralwer
        mysql = cralwer.settings['MYSQL_INFO']      #获取变量
        self.mysql = mydb.Mydb(mysql['MYSQL_HOST'], mysql['MYSQL_USER'], mysql['MYSQL_PASS'], mysql['MYSQL_DB'])    #初始化连接

    @classmethod  # 变成类方法
    def from_crawler(cls, cralwer):  # 定义一个方法
        return cls(cralwer)  # 实例化一个对象,返回

    def process_request(self,request,spider):
        res = self.mysql.query('select * from xici ORDER BY rand() limit 1')    #随机排序并只取一个值,查询语句用query方法
        proxy = res[0]
        proxy = 'http://' + proxy['host'] + ':' + str(proxy['port'])
        request.meta['proxy'] = proxy   ###设置代理

		
#代理
class RandomProxy(object):
    def __init__(self, cralwer):  ##初始化useragent,接收cralwer
        # 全局爬虫对象
        self.crawler = cralwer
        mysql = cralwer.settings['MYSQL_INFO']      #获取变量
        self.mysql = mydb.Mydb(mysql['MYSQL_HOST'], mysql['MYSQL_USER'], mysql['MYSQL_PASS'], mysql['MYSQL_DB'])    #初始化连接

    @classmethod  # 变成类方法
    def from_crawler(cls, cralwer):  # 定义一个方法
        return cls(cralwer)  # 实例化一个对象,返回

    def process_request(self,request,spider):
        res = self.mysql.query('select * from xici ORDER BY rand() limit 1')    #随机排序并只取一个值,查询语句用query方法
        proxy = res[0]
        proxy = 'http://' + proxy['host'] + ':' + str(proxy['port'])
        request.meta['proxy'] = proxy   ###设置代理

		
class PhantomjsMiddleware(object):
    def __init__(self):
        self.browser = webdriver.PhantomJS()  # 需要配置phantom环境变量，只初始化一次提高效率
    def process_request(self,request,spider):
        '''
        :param request: 请求对象
        :param spider: 蜘蛛对象
        :return:
        '''
        if request.meta.get('phantomjs',None):      #判断True和Flase
            # print(request.url)
            # browser = webdriver.PhantomJS() # 需要配置phantom环境变量
            self.browser.get(request.url)           #request.url拿到的是taobao.py中60行中的url
            time.sleep(1)
            html = self.browser.page_source         #源代码
            # browser.quit()
            # print(html)
            response = HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)

            return response


		
class ScrapyTestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyTestDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
