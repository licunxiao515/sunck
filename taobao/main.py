from scrapy import cmdline

#执行一个爬虫
#split按照空格拆分成列表,列表传入execute里
cmdline.execute('scrapy crawl taobao'.split())