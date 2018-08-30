# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyTestPipeline(object):
    #负责处理item数据,存入文件或者存入数据库
    def process_item(self, item, spider):
        return item
		
class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','123456','temp',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class TaobaoMysqlPipeline(MysqlPipeline):
    def process_item(self, item, spider):
        if spider.name == 'taobao':
        #构建sql语句
            sql = 'insert into taobao(pic_url,detail_url,shop_name,goods_name,view_sales,item_loc,price,crawl_time) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update price=values(price),shop_name=VALUES(shop_name)'
            try:
                self.cursor.execute(sql, (
                item["pic_url"], item["detail_url"], item["shop_name"], item["goods_name"], item["view_sales"], item["item_loc"], item["price"], item["crawl_time"]))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
                print('执行语句失败')
                # 返回交给下一个管道文件处理
        return item