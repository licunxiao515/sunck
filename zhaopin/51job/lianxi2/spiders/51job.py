# -*- coding: utf-8 -*-
import scrapy
from lianxi2.items import Lianxi2Item
from scrapy_redis.spiders import RedisSpider

class A51jobSpider(RedisSpider):
    name = '51job'
    allowed_domains = ['51job.com']
    # start_urls = ['http://www.51job.com/']
    redis_key = '51jobspider:urls'
    base_url = 'http://search.51job.com/list/010000%252C00,000000,0000,00,9,99,%2B,2,'

    def parse(self, response):
        for i in range(1,5):
            i = str(i)
            list = [self.base_url,i,'.html']
            fulurl = "".join(list)
            print(fulurl)
            yield scrapy.Request(url=fulurl,callback=self.parse_list)

    #首页
    def parse_list(self ,response):
        url_detail = response.xpath('//div[@class="dw_table"]/div[@class="el"]/p/span/a/@href').extract()
        for url in url_detail:
            url = url.split('?')[0]     #优化详情页链接
            yield scrapy.Request(url=url,callback=self.parse_list_detail)

   #详情页
    def parse_list_detail(self,response):
        item = Lianxi2Item()
        # print(response.text)
        url = response.url      #主键地址
        pname = response.xpath('//div[@class="tHeader tHjob"]/div/div/h1/text()').extract()[0]  #职位名称
        gs_name = response.xpath('//div[@class="tHeader tHjob"]/div/div/p/a/text()').extract()[0]  #公司名称
        money = response.xpath('//div[@class="tHeader tHjob"]/div/div/strong/text()').extract()[0]  #月薪
        zyear = response.xpath('//div[@class="tBorderTop_box bt"]/div/div/span[1]/text()').extract()[0]  #工作经验
        education = response.xpath('//div[@class="tBorderTop_box bt"]/div/div/span[2]/text()').extract()[0]  #最低学历

        address = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()  #公司地址
        address = ''.join(address)
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