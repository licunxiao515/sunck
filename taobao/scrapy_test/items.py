# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    pic_url = scrapy.Field()
    detail_url = scrapy.Field()
    shop_name = scrapy.Field()
    goods_name = scrapy.Field()
    view_sales = scrapy.Field()
    item_loc = scrapy.Field()
    price = scrapy.Field()
    crawl_time = scrapy.Field()