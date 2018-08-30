# -*- coding: utf-8 -*-
import scrapy
from urllib import request
import re
import json
import jsonpath
from scrapy_test.items import TaobaoItem
import datetime

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    base_url = 'https://s.taobao.com/search?q=电子琴&s=%d'
    start_urls = ['https://www.taobao.com']

    def parse(self, response):
        # 生成列表页请求
        for i in range(0,1,44):
            fullurl = self.base_url % i
            yield scrapy.Request(fullurl,callback=self.parselist,meta={'phantomjs':False})

    # 解析列表页
    def parselist(self,response):
        print(type(response))
        # 获取所有商品div
        html = response.text
        data_pat = re.compile(r'g_page_config = (.*)\n')
        res = data_pat.search(html)

        if res is not None:
            data = res.group(1).strip(';')      ###去掉;
            data = json.loads(data)
            res = jsonpath.jsonpath(data,'$..auctions.*')
            for goods in res:
                item = TaobaoItem()
                shop_name = goods['nick']
                goods_name = goods['title']

                view_sales = goods['view_sales']
                view_sales = self.get_number(view_sales)

                detail_url = goods['detail_url']
                detail_url = request.urljoin(response.url,detail_url)

                item_loc = goods['item_loc']
                price = goods['view_price']
                pic_url = goods['pic_url']
                pic_url = request.urljoin(response.url,pic_url)

                # 加载数据到数据模型中
                item["pic_url"] = pic_url
                item["detail_url"] = detail_url
                item["shop_name"] = shop_name
                item["goods_name"] = goods_name
                item["view_sales"] = view_sales
                item["item_loc"] = item_loc
                item["price"] = price
                item['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # 默认请求地址不允许重复
                # 设置dont_filter 为True   允许重复请求
                yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'data':item,'phantomjs':True},dont_filter=True)

    ###详情页
    def parse_detail(self,response):        #这个response是自己构造的
        item = response.request.meta['data']
        # print(response.text)
        # 提取月销量
        if 'tm-count' in response.text: # 天猫页面
            info = response.xpath('//span[@class="tm-count"]/text()').extract()
            permonth = info[0]
            commentcon = info[1]
            # print('天猫',permonth, commentcon)

        else: # 淘宝页面
            permonth = response.xpath('//strong[@id="J_SellCounter"]/text()').extract()[0]
            commentcon = response.xpath('//strong[@id="J_RateCounter"]/text()').extract()[0]

            # print('淘宝',permonth, commentcon)

        item['permonth'] = permonth
        item['commentcon'] = commentcon

        yield item


    def get_number(self,value):
        number_pat = re.compile(r'\d+')
        res = number_pat.search(value)
        if res is not None:
            return res.group()
        else:
            return 0

