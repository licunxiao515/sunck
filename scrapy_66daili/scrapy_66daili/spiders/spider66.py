# -*- coding: utf-8 -*-
import scrapy
from scrapy_66daili.items import Proxy66Item

class Spider66Spider(scrapy.Spider):
    name = 'spider66'
    allowed_domains = ['66ip.cn']
    start_urls = ['http://66ip.cn/']
    base_url = 'http://www.66ip.cn/%d.html'

    def parse(self, response):
        # print(response.status)
        for i in range(1,2+1):
            fullurl = self.base_url % i
            yield scrapy.Request(url=fullurl,callback=self.parselist)

    def parselist(self,response):
        proxy_list = response.xpath('//div[@align="center"]//tr')[1:]
        print(proxy_list)
        for proxy in proxy_list:
            item = Proxy66Item()
            info = proxy.xpath('./td/text()').extract()
            host = info[0]      #ip
            port = info[1]      #端口号
            print(host,port)
            item['host'] = host
            item['port'] = port

            yield item


