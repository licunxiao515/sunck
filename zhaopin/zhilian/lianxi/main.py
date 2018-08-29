from scrapy import cmdline
import os
# cmdline.execute('scrapy crawl zhilian'.split())
os.chdir('C:\pythonenv\lianxi\lianxi\spiders')
cmdline.execute('scrapy runspider zhilian.py'.split())