# -*- coding: utf-8 -*-
import scrapy
from lianxi4.items import Lianxi4Item
from scrapy_redis.spiders import RedisSpider

class ZhonghuayingcaiSpider(RedisSpider):
    name = 'zhonghuayingcai'
    allowed_domains = ['chinahr.com']
    # start_urls = ['http://www.chinahr.com/']
    redis_key = 'chinahrspider:urls'
    base_url = 'http://www.chinahr.com/sou/?page=%d'

    def parse(self, response):
        for i in range(1,5):
            fulurl = self.base_url % i
            yield scrapy.Request(url=fulurl,callback=self.parse_list)

    def parse_list(self,response):
        url_id_data = response.xpath('//div[@class="jobList"]/ul/li/span[1]/a/@href').extract()
        for url_id in url_id_data:
            url_id = url_id.split('?')[0]
            yield scrapy.Request(url=url_id,callback=self.parse_list_detail)

    def parse_list_detail(self,response):
        item = Lianxi4Item()
        url = response.url
        pname = response.xpath('//div[@class="base_info"]/div/h1/span/text()').extract()[0]
        gs_name = response.xpath('//div[@class="job-company jrpadding"]/h4/a/text()').extract()[0]
        money  = response.xpath('//div[@class="job_require"]/span[1]/text()').extract()[0]
        zyear  = response.xpath('//div[@class="job_require"]/span[5]/text()').extract()[0]
        education  = response.xpath('//div[@class="job_require"]/span[4]/text()').extract()[0]
        address  = response.xpath('//div[@class="job_require"]/span[2]/text()').extract()[0]
        # print(url,pname,gs_name,money,zyear,education,address)

        item['url'] = url       #主键地址
        item['pname'] = pname   #职位名称
        item['gs_name'] = gs_name   #公司名称
        item['money'] = money       #月薪
        item['zyear'] = zyear       #工作经验
        item['education'] = education       #最低学历
        item['address'] = address           #公司地址

        return item