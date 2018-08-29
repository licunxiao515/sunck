# -*- coding: utf-8 -*-
import scrapy
import requests
from urllib import request
import time
import json

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/#signin']

    login_url = 'https://www.zhihu.com/login/phone_num'

    custom_settings = {
        'COOKIES_ENABLED' : True
    }

    headers = {
        "Host": "www.zhihu.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #"Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    def start_requests(self):
        url = 'https://www.zhihu.com/#signin'
        yield scrapy.Request(url=url,headers=self.headers)

    def parse(self, response):
        #提取xsrf,xsrf为保护码
        xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract()[0]

        #code_url验证码，int(time.time() * 1000)为%d的值，%d为时间戳
        code_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % int(time.time() * 1000)
        yield scrapy.Request(code_url,callback=self.parse_code,meta={'xsrf':xsrf},headers=self.headers)

    def parse_code(self,response):
        xsrf = response.meta['xsrf']
        with open('zhihu.gif','wb') as f:
            f.write(response.body)

        code = input('输入验证码：')

        data = {
            '_xsrf' : xsrf,
            'phone_num' : '18600672750',
            'password' : '1234qwer',
            'captcha' : code,
        }

        yield scrapy.FormRequest(self.login_url,formdata=data,headers=self.headers,callback=self.parse_home)

    #解析响应
    def parse_home(self,response):
        data = json.loads(response.text)
        if '成功' in data['msg'] :
            print('登陆成功，继续请求吧')
        else:
            print('登陆失败')
            print(json.dumps(data,ensure_ascii=False,indent=4))
