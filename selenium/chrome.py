from selenium import webdriver
import time

chrome = webdriver.Chrome(executable_path='C:/phantomjs-2.1.1-windows/bin/chromedriver.exe')    #初始化浏览器
chrome.get('http://www.weibo.com')
time.sleep(10)

#微博登陆
chrome.find_element_by_id('loginname').send_keys('13401000750')     #账号
chrome.find_element_by_css_selector('input[type="password"]').send_keys('i13401000750') #密码

chrome.find_element_by_css_selector('div[class="info_list login_btn"] a').click()   #登陆

