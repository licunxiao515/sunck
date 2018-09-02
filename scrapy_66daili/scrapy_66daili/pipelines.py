# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class Scrapy66DailiPipeline(object):
    def process_item(self, item, spider):
        return item



class Spider66MysqlPipeline(object):
    def __init__(self, cralwer):  ##初始化useragent,接收cralwer
        # 全局爬虫对象
        self.crawler = cralwer
        # 创建数据库操作对象
        mysql = self.crawler.settings['MYSQL_INFO']
        self.conn = pymysql.connect(mysql['MYSQL_HOST'],mysql['MYSQL_USER'],mysql['MYSQL_PASS'],mysql['MYSQL_DB'],charset='utf8')
        self.cursor = self.conn.cursor()

    @classmethod  # 变成类方法
    def from_crawler(cls, cralwer):  # 定义一个方法
        return cls(cralwer)  # 实例化一个对象,返回

    def process_item(self, item, spider):
        try:
            print('链接数据库成功')
            sql = 'insert into spiderip(host,port) VALUES(%s,%s) on duplicate key update port=VALUES(port)'
            data = (item['host'], item['port'])
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        return item