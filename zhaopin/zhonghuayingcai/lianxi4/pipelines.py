# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Lianxi4Pipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','123456','temp',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class ChinahrMysqlPipeline(MysqlPipeline):
    def process_item(self,item,spider):
        if spider.name == 'zhonghuayingcai':
            sql = 'insert into chinahr_job(url,pname,gs_name,money,zyear,education,address)' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s) on duplicate key update money=values(money),education=VALUES(education),address=values(address)'
            try:
                self.cursor.execute(sql,(item["url"],item["pname"],item['gs_name'],item["money"],item["zyear"],item["education"],item["address"]))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
                print('执行语句失败')
        #返回一个管道文件处理
        return item
