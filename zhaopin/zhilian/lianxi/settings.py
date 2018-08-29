# -*- coding: utf-8 -*-

# Scrapy settings for lianxi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianxi'

SPIDER_MODULES = ['lianxi.spiders']
NEWSPIDER_MODULE = 'lianxi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianxi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianxi.middlewares.LianxiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'lianxi.middlewares.RandomUserAgent': 1,
    'lianxi.middlewares.RandomProxy': 2,
}
#
# PROXIES = [
#     {'host' : 'http://61.135.217.7:80'},  #主机地址
#     {'host' : 'https://61.135.217.7:80'},
# ]

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'lianxi.pipelines.ZhilianMysqlPipeline': 1,
    'scrapy_redis.pipelines.RedisPipeline': 2,  # 数据加入到redis里
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


UA_TYPE = 'random'
#
MYSQL_INFO = {
    'MYSQL_HOST' : '127.0.0.1',
    'MYSQL_USER' : 'root',
    'MYSQL_PASS' : '123456',
    'MYSQL_DB'  : 'temp',
}

#定义代理，用字典
PROXIES = [
    {'host' : 'http://14.118.252.202:6666'},  #主机地址
    {'host' : 'https://14.118.255.249:6666'},
]


# 配置scrapy-redis 去重类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 配置scrapy-redis 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 调度器是否能中止
SCHEDULER_PERSIST = True

# 请求队列模式
# 按照优先级调度请求  request  priority属性（默认0）  q = (0,0,0,1,1,3)
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 按照FIFO 队列 调度请求
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 按照LIFO 队列 调度请求
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"



# LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# redis 连接信息
REDIS_HOST = '192.168.136.130'      #ip
REDIS_PORT = 6379                      #端口号