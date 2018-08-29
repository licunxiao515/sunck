# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    #覆盖全局配置项
    custom_settings = {
        'COOKIES_ENABLED' : True
    }

    headers = {
        "Host": "www.renren.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.renren.com/241873187/profile",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        #headers里识别不了cookie,所以需要把cookie拿出来
        # "Cookie": "anonymid=jgdof2ax-y2ex78; _r01_=1; depovince=GW; jebecookies=f55c48c5-dc62-4955-9d76-bfeefd252d6b|||||; ick_login=e62b46d8-2727-4e7f-a5b8-3b86b40e7d46; _de=8290071A058DEE6B7D49636C5D3D4B7E696BF75400CE19CC; p=5bc2266d3b826adce88aa131647913677; first_login_flag=1; ln_uact=523112886@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20120401/2305/h_main_iNx4_5f42000361452f75.jpg; t=f0cdaa582721e9e907038f22a22aca3d7; societyguester=f0cdaa582721e9e907038f22a22aca3d7; id=241873187; xnsid=e780764b; loginfrom=syshome; ch_id=10016; jebe_key=ad9039c0-5e7d-476f-a0ea-bad2c4e67a7a%7Cf9efb7b9ff070639325d7a657bfab146%7C1529419370322%7C1%7C1529419374569; wpsid=15216817989651; wp_fold=0",
    }

    cookie = {
        "anonymid": "jgdof2ax-y2ex78",
        "_r01_": "1",
        "depovince": "GW",
        "_de": "8290071A058DEE6B7D49636C5D3D4B7E696BF75400CE19CC",
        "ln_uact": "523112886@qq.com",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn521/20120401/2305/h_main_iNx4_5f42000361452f75.jpg",
        "jebe_key": "ad9039c0-5e7d-476f-a0ea-bad2c4e67a7a%7Cf9efb7b9ff070639325d7a657bfab146%7C1529419370322%7C1%7C1529419374569",
        "jebecookies": "5f228ac3-a384-414b-ad82-9237e0f33b5b|||||",
        "JSESSIONID": "abcOg314hk9pwhIkPTBqw",
        "ick_login": "01ae887d-829e-496d-99ee-fd6a4817aa38",
        "p": "3816648fa760c056f89796b13edab3077",
        "first_login_flag": "1",
        "t": "5026860894a10fa8c1b34c49135f54ab7",
        "societyguester": "5026860894a10fa8c1b34c49135f54ab7",
        "id": "241873187",
        "xnsid": "e4495372",
        "loginfrom": "syshome",
        "ch_id": "10016",
        "wp_fold": "0",
    }

    def parse(self, response):
        home_url = 'http://www.renren.com/241873187/profile'
        yield scrapy.Request(url=home_url,headers=self.headers,cookies=self.cookie,callback=self.parse_home)

    def parse_home(self,response):
        print(response.text)        #提取内容

