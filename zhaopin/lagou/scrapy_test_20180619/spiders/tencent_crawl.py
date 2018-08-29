# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor         #提取网页超链接的类
from scrapy.spiders import CrawlSpider, Rule            #Rule规格


class TencentCrawlSpider(CrawlSpider):
    name = 'tencent_crawl'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']        #起点

    rules = (
        #LinkExtractor提取链接，把提取的链接全部加入请求队列（如果里边为空值提取所有的）
        #allow正则规格,匹配的是a标签href内容,如果里边是元祖，或者的关系规格，求得是并集的关系
        # Rule(LinkExtractor(allow=(r'game.hao123',r'stocknew')), callback='parse_item', follow=False),
        #和上边的意思一样，如果follow=True跟进提取（提取的页面链接如果还有符合匹配信息，继续提取）
        Rule(LinkExtractor(allow=(r'hr.tencent.com/position.php')), follow=True),
        Rule(LinkExtractor(allow=(r'hr.tencent.com/social.php')), follow=True),
        Rule(LinkExtractor(allow=(r'hr.tencent.com/position_detail.php')), callback='parse_item', follow=False,process_links='process_links'),
        # follow 如果为True（默认是True） 则会在跟进链接中继续匹配符合正则规则的超链接
        #如果allow=()为空值，follow=True,爬取的是全网链接
    )

    ##去重函数
    def process_links(self,links):
        #links接受的是列表[Link,Link]，里边是Link对象，Link对象里边有个属性是url
        for link in links:
            if '&' in link.url: #去掉&后边的数据
                link.url = link.url.split('&')[0]
            print(link.url)
            print(500)
        return links


    #详情页解析
    def parse_item(self, response):
        print(response.status)
        print(100)
        print(response.url)
        print(response.status)
        # title = response.xpath('//title/text()').extract()[0]
        # url = response.url.extract()
        # item = {
        #     'title' : title
        # }
        # yield item  #走管道pipelines