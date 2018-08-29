# -*- coding: utf-8 -*-
import scrapy
from lianxi3.items import Lianxi3Item
from scrapy_redis.spiders import RedisSpider

class LeipinSpider(RedisSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    # start_urls = ['http://www.liepin.com/']
    redis_key = 'liepinspider:urls'
    base_url = 'http://www.liepin.com/zhaopin/?curPage=%d'

    def parse(self, response):
        for i in range(0,5):
            fulurl = self.base_url % i
            yield scrapy.Request(url=fulurl,callback=self.parse_list)

    #获取url
    def parse_list(self,response):
        url_id = response.xpath('//div[@class="job-info"]/h3/a/@href').extract()
        for url_id_list in url_id:
            yield scrapy.Request(url=url_id_list,callback=self.parse_list_detail)

    #获取详情页
    def parse_list_detail(self,response):
        item = Lianxi3Item()
        url = response.url
        pname = response.xpath('//div[@class="title-info"]/h1/text()').extract()[0]
        gs_name = response.xpath('//div[@class="title-info"]/h3/a/text()').extract()[0]
        money = response.xpath('//div[@class="job-title-left"]/p/text()').extract()[0]
        money = self.remove_splash(money)
        zyear = response.xpath('//div[@class="job-qualifications"]/span[2]/text()').extract()[0]
        education = response.xpath('//div[@class="job-qualifications"]/span[1]/text()').extract()[0]
        address = response.xpath('//div[@class="new-compwrap"]/ul/li[3]/text()').extract()[0]

        item['url'] = url       #主键地址
        item['pname'] = pname   #职位名称
        item['gs_name'] = gs_name   #公司名称
        item['money'] = money       #月薪
        item['zyear'] = zyear       #工作经验
        item['education'] = education       #最低学历
        item['address'] = address           #公司地址

        return item

    def remove_splash(self,value):
        return value.replace('/','').strip()