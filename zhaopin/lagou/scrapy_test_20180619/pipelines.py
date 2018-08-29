# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyTest20180619Pipeline(object):
    def __init__(self):
        self.f = open('job','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(item['title'] + '\n')
        return item

    #在爬虫关闭时调用爬虫关闭
    def close_spider(self,spider):
        self.f.close()

