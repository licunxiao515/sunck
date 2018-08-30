# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_test'

SPIDER_MODULES = ['scrapy_test.spiders']
NEWSPIDER_MODULE = 'scrapy_test.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_test (+http://www.yourdomain.com)'


# Obey robots.txt rules
#是否遵守搜索引擎协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#设置并发量
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载延迟
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#每个域名最大限制并发数
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#每个ip最大并发数
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#是否启用cookie,默认是True
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#默认全局请求头设置
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#图里的红色中间件
#SPIDER_MIDDLEWARES = {
#    'scrapy_test.middlewares.ScrapyTestSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#下载中间件，图里黄色的
DOWNLOADER_MIDDLEWARES = {
    #数字是中间件执行顺序，数字越小，优先级越大
    'scrapy_test.middleware.RandomUserAgent': 1,
    'scrapy_test.middleware.RandomProxy': 2,
    'scrapy_test.middleware.PhantomjsMiddleware': 3,   #PhantomjsMiddleware是中间件类
}
UA_TYPE = 'random'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
    ##数字是管道文件执行顺序，数字越小，优先级越大
ITEM_PIPELINES = {
	'scrapy_test.pipelines.TaobaoPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_INFO = {
    'MYSQL_HOST' : '127.0.0.1',
    'MYSQL_USER' : 'root',
    'MYSQL_PASS' : '123456',
    'MYSQL_DB'  : 'temp',
}