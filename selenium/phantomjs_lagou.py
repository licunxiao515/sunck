from selenium import webdriver
import time
from lxml import etree

# 设置user-agent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)
browser = webdriver.PhantomJS(desired_capabilities=dcap)



def getIndex():
    browser.get('https://www.lagou.com/jobs/list_python')
    time.sleep(3) # 等待
    html = browser.page_source      #获取当前页面代码
    # 首次获取数据
    parsePage(html)

    # 循环分页获取数据
    while True:
        browser.find_element_by_class_name('pager_next ').click()     #下一页
        time.sleep(0.5)
        html = browser.page_source          # 获取当前页面代码
        parsePage(html)
        if 'pager_next_disabled' in html:       #下一页到头，点击不了。break
            break

def parsePage(html):
    html = etree.HTML(html)     # 返回xpath 对象，支持xpath规则进行匹配
    job_li = html.xpath('//ul[@class="item_con_list"]/li')  #找到工作的所有li
    for li in job_li:
        job_name = li.xpath('.//h3/text()')[0]
        salary = li.xpath('.//span[@class="money"]/text()')[0]
        address = li.xpath('.//span[@class="add"]/em/text()')[0]
        date_pub = li.xpath('.//span[@class="format-time"]/text()')[0]
        print(job_name,salary,address,date_pub)



# browser.save_screenshot('lagou.png')
if __name__ == '__main__':
    getIndex()
    browser.quit()