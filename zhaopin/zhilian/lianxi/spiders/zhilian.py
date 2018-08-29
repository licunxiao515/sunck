# -*- coding: utf-8 -*-
import scrapy
import json
import jsonpath,requests
from lianxi.items import LianxiItem
from scrapy_redis.spiders import RedisSpider

class ZhilianSpider(RedisSpider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    # start_urls = ['http://www.zhaopin.com/']
    redis_key = 'zhilianspider:urls'
    base_url = 'http://fe-api.zhaopin.com/c/i/sou?start=%d'



    def parse(self, response):
        for i in range(0,240 + 1,60):
            fulurl = self.base_url % i
            yield scrapy.Request(url=fulurl,callback=self.parse_list)

    def parse_list(self,response):
        json_url = response.text
        json_data = json.loads(json_url)        #转换为字典
        # print(json_data)
        res = jsonpath.jsonpath(json_data,'$..positionURL') #获取详情页地址
        for res_url in res:
            yield scrapy.Request(url=res_url, callback=self.parse_list_detail)

    #详情页
    def parse_list_detail(self,response):
        # print(response.request.headers)
        # print(response.meta)

        item = LianxiItem()

        url = response.url     #主键地址
        # print(response.url)
        # print(response.text)
        pname = response.xpath('//div[@class="inner-left fl"]/h1/text()').extract()[0]  #职位名称
        gs_name = response.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()[0] #公司名称

        x_list = response.xpath('//div[@class="terminalpage-left"]/ul')
        money= x_list.xpath('//li[1]/strong/text()').extract()[0]  #月薪
        zyear = x_list.xpath('//li[5]/strong/text()').extract()[0]    #工作经验
        education = x_list.xpath('//li[6]/strong/text()').extract()[0]    #最低学历

        address = response.xpath('//div[@class="tab-inner-cont"]/h2/text()').extract()[0]    #公司地址
        address = self.remove_splash(address)



        item['url'] = url       #主键地址
        item['pname'] = pname   #职位名称
        item['gs_name'] = gs_name   #公司名称
        item['money'] = money       #月薪
        item['zyear'] = zyear       #工作经验
        item['education'] = education       #最低学历
        item['address'] = address           #公司地址


        return item
    def remove_splash(self, value):
        return value.replace('/', '').strip()