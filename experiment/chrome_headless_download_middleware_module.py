from scrapy import downloadermiddlewares
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

import os

from lxml import etree


'''
用法：
粘贴到DownloadMiddleware中
在settings.py(zhuge是run.py)中注册
'''


class chrome_headless(object):

    # 将初始化selenium使chrome_headless生效
    # 返回值self.chen_opener为入口
    @classmethod
    def process_request(cls, request, spider):
        chen_chrome_options = Options()
        chen_chrome_options.add_argument('--headless')
        chen_chrome_options.add_argument('--disable-gpu')
        chen_chrome_options.add_argument('lang=zh_CN.UTF-8')
        chen_chrome_options.add_argument('user-agent = "ozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)"')
        chen_chrome_options.add_argument('Accept = "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"')
        prefs = {"profile.managed_default_content_settings.images": 2}
        chen_chrome_options.add_experimental_option("prefs", prefs)
        chen_opener = webdriver.Chrome(chrome_options = chen_chrome_options,
                                       # executable_path = '/home/chenyu/chensf/chromedriver')
                                       executable_path = '../../../../plugin/chromedriver')

        # 接受一个网址，返回js渲染后的源码
        chen_opener.get(request.url)
        content = chen_opener.page_source.encode('utf-8')

        chen_opener.close()
        chen_opener.quit()

        print 'already cross selenium'

        # return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)