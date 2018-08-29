from selenium import webdriver
import time

############phantomjs 设置user-agent  固定格式
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 设置user-agent
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)
browser = webdriver.PhantomJS(desired_capabilities=dcap,executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
###########     end     ####


browser.get('https://www.weibo.com')

time.sleep(10)
browser.save_screenshot('weibo.png')
print(browser.page_source)
# # 输入账户名和密码
# browser.find_element_by_id('loginname').send_keys('18600672750')      #通过id查找，send_keys为输入框的内容（账号）
# chrome.find_element_by_css_selector('input[type="password"]').send_keys('1234qwer')      #没有id，通过class查找，send_keys为输入框的内容（密码）

# # 点击登陆
# browser.find_element_by_class_name('W_btn_a btn_32px ').click()

# time.sleep(1)
# browser.save_screenshot('weibo.png')

browser.quit()