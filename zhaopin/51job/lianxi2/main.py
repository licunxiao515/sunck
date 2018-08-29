from scrapy import cmdline
import os
# cmdline.execute('scrapy crawl 51job'.split())
os.chdir('C:\pythonenv\lianxi2\lianxi2\spiders')
cmdline.execute('scrapy runspider 51job.py'.split())