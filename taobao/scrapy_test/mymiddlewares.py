from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time

class PhantomjsMiddleware(object):
    def __init__(self):
        self.browser = webdriver.PhantomJS()  # 需要配置phantom环境变量，只初始化一次提高效率
    def process_request(self,request,spider):
        '''
        :param request: 请求对象
        :param spider: 蜘蛛对象
        :return:
        '''
        if request.meta.get('phantomjs',None):      #判断True和Flase
            # print(request.url)
            # browser = webdriver.PhantomJS() # 需要配置phantom环境变量
            self.browser.get(request.url)           #request.url拿到的是taobao.py中60行中的url
            time.sleep(1)
            html = self.browser.page_source         #源代码
            # browser.quit()
            # print(html)
            response = HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)

            return response


