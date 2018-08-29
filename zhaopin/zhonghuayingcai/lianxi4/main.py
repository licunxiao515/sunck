from scrapy import cmdline
import os
# cmdline.execute('scrapy crawl zhonghuayingcai'.split())
os.chdir('C:\pythonenv\lianxi4\lianxi4\spiders')
cmdline.execute('scrapy runspider zhonghuayingcai.py'.split())