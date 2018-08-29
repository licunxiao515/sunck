from selenium import webdriver
import time
from lxml import etree

chrome = webdriver.Chrome(executable_path='C:/phantomjs-2.1.1-windows/bin/chromedriver.exe')

def getPage():
    chrome.get('https://www.douyu.com/directory/all')       #爬取斗鱼所有房间
    time.sleep(3)
    html = chrome.page_source
    parsePage(html)

    while 'shark-pager-disable-next' not in html:       #最后一页的条件
        chrome.find_element_by_class_name('shark-pager-next').click()
        time.sleep(0.5)
        html = chrome.page_source
        parsePage(html)

def parsePage(html):
    html = etree.HTML(html)
    room_li = html.xpath('//ul[@id="live-new-show-content-box"]/li | //ul[@id="live-list-contentbox"]/li')
    for room in room_li:
        room_name = room.xpath('.//h3/text()')[0].strip()
        room_type = room.xpath('.//span[@class="tag ellipsis"]/text()')[0].strip()
        nick = room.xpath('.//span[@class="dy-name ellipsis fl"]/text()')[0].strip()
        number = room.xpath('.//span[@class="dy-num fr"]/text()')
        number = number[0].strip() if number else 0 #如果number有数据按照number[0].strip()存储，如果没有数据存入0
        #存入数据库，纯数字
        if number != 0 and '万' in number:
            number = number.strip('万')
            number = float(number) * 10000

        print(room_name,room_type,nick,number)

if __name__ == '__main__':
    getPage()