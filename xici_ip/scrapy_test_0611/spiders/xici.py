# -*- coding: utf-8 -*-
import scrapy
from scrapy_test_0611 import settings
import random
from scrapy_test_0611.items import XiciItem
class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']
    base_url = 'http://www.xicidaili.com/nn/%d'

    def parse(self,response):
        headers = {}
        for i in range(1,10 + 1):
            fullurl =self.base_url % i
            yield scrapy.Request(url=fullurl,callback=self.parse_list)

    def parse_list(self,response):
        print(response.status)
        proxy_list = response.xpath('//table[@id="ip_list"]//tr')[1:]#提取信息,把第一个去掉
        for proxy in proxy_list:
            item = XiciItem()   #实例化items.py的对象
            info = proxy.xpath('.//td/text()').extract()
            # print(info)
            host = info[0]  #ip地址
            # print(host)
            port = info[1]  #端口号
            item['host'] = host #传入items.py文件中XiciItem属性值
            item['port'] = port


            ###执行管道文件pipelines.py
            yield item