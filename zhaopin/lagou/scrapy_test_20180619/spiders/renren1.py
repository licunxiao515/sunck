# -*- coding: utf-8 -*-
import scrapy


class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']
    login_url = "http://www.renren.com/PLogin.do"

    #覆盖全局配置项
    custom_settings = {
        'COOKIES_ENABLED' : True
    }
    #默认会把start_urls 的地址全部转化为scrapy.Request对象
    def start_requests(self):
        #发送post请求
        data = {
            'email' : '523112886@qq.com',
            'password' : 'i13683546343',
        }
        #不指定回掉则调用parse
        yield scrapy.FormRequest(url=self.login_url,formdata=data)#formdata为提交的表单数据

    def parse(self, response):
        print(response.text)
