# -*- coding: utf-8 -*-
import scrapy
from scrapy_test_0611 import settings       #####导入settings模块
#from scrapy.conf import settings
import random


class BaiduSpider(scrapy.Spider):
    name = 'xicidaili'
    #allowed_domains 允许爬虫有效域
    # allowed_domains = ['baidu.com']         ####如果为空值，不限制访问的域名
    allowed_domains = ['baidu.com','xicidaili.com']     ####列表形势，可以多个域名
    start_urls = ['http://baidu.com/']                  ####起始地址
    base_url = 'http://www.xicidaili.com/nn/%d'  #西祠代理

    def parse(self, response):
        headers = {}        #定义空字典
        for i in range(1,10 + 1):
            fullurl = self.base_url % i
            #发起请求，先走中间件
            yield scrapy.Request(url=fullurl,callback=self.parse_list)     ##callback响应码

    ###parse.list每一页的响应状态
    def parse_list(self,response):
        print(response.status)
        print(response.request.headers)
