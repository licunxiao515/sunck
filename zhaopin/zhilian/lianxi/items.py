# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianxiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    pname = scrapy.Field()
    gs_name = scrapy.Field()
    money = scrapy.Field()
    zyear = scrapy.Field()
    education = scrapy.Field()
    address = scrapy.Field()





