from selenium import webdriver
import time
from lxml import etree
from urllib import request
import uuid

chrome = webdriver.Chrome(executable_path='C:/phantomjs-2.1.1-windows/bin/chromedriver.exe')

chrome.get('http://image.baidu.com/search/index?tn=baiduimage&word=%E5%B0%8F%E7%BE%8E')     #%E5%B0%8F%E7%BE%8E  urlencode,没有转换
time.sleep(5)

def getPage():
    html = chrome.page_source
    parsePage(html) # 首次解析图片

    # 向下滚动
    while True:         #持续的获取图片
        chrome.execute_script('scrollTo(0,document.body.scrollHeight)') #滚动到底部，加载瀑布流用
        time.sleep(2)
        html = chrome.page_source
        parsePage(html)

def parsePage(html):
    html = etree.HTML(html)
    img_url = html.xpath('//div[@class="imgpage"][last()]//ul//li/@data-objurl')    #图片地址，滚动一次增加一个DIV，所以获取最后一个div[last()]
    # print(img_url)
    for url in img_url:
        fname = str(uuid.uuid4())       #uuid算法，随机起名用，调用后uuid转换成str类型
        print('downloading...%s' % url)   #调试用，可以看到哪报错
        try:
            request.urlretrieve(url,'./baiduimg/' + fname + '.jpg')     #下载图片
        except Exception as e:
            print('遇到广告')

if __name__ == '__main__':
    getPage()